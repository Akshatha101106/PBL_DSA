#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <unordered_map>
#include <cctype>
#include "json.hpp"

using namespace std;
using json = nlohmann::json;

/* ===================== STRUCTURES ===================== */

struct Candidate
{
    string name;
    string branch;
    set<string> skills; // normalized skills
};

struct CompanyResult
{
    string company;
    string role;
    double score;
    vector<string> matched_skills;
    vector<string> skill_gap;
};

/* ===================== PRIORITY QUEUE ===================== */

struct Compare
{
    bool operator()(const CompanyResult &a,
                    const CompanyResult &b)
    {
        return a.score < b.score; // max heap
    }
};

/* ===================== NORMALIZE STRING ===================== */

string normalize(string s)
{
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c)
              { return tolower(c); });
    return s;
}

/* ===================== PARSE CANDIDATE ===================== */

Candidate parse_candidate(const json &resume)
{
    Candidate c;
    c.name = resume["candidate_info"]["Name"];
    c.branch = resume["candidate_info"]["Branch"];

    for (auto &category : resume["Skills"].items())
    {
        for (auto &skill : category.value())
        {
            c.skills.insert(normalize(skill));
        }
    }
    return c;
}

/* ===================== QUALIFICATION MATCH ===================== */

bool qualification_match(vector<string> company_qual,
                         const string &candidate_branch)
{

    // Handle "Any" qualification
    for (auto &q : company_qual)
    {
        string qq = normalize(q);
        if (qq == "any" || qq == "any graduate")
            return true;
    }

    // Normalize qualifications
    for (auto &q : company_qual)
        q = normalize(q);

    string branch = normalize(candidate_branch);

    sort(company_qual.begin(), company_qual.end());

    return binary_search(company_qual.begin(),
                         company_qual.end(),
                         branch);
}

/* ===================== SCORE CALCULATION ===================== */

double calculate_score_10(const vector<string> &required,
                          const vector<string> &preferred,
                          const Candidate &candidate,
                          int &matched_required_out)
{

    double score = 0.0;
    matched_required_out = 0;

    // Qualification weight
    score += 3.0;

    // Required skills (max 5)
    for (auto &s : required)
        if (candidate.skills.count(normalize(s)))
            matched_required_out++;

    if (!required.empty())
        score += 5.0 * matched_required_out / required.size();

    // Preferred skills (max 2)
    int matched_preferred = 0;
    for (auto &s : preferred)
        if (candidate.skills.count(normalize(s)))
            matched_preferred++;

    if (!preferred.empty())
        score += 2.0 * matched_preferred / preferred.size();

    return score;
}

/* ===================== MAIN ===================== */

int main()
{

    cout << "PROGRAM STARTED\n";

    json company_data, student_data;

    ifstream OpenCompanyFile("company_job_data_to_cpp.json");
    ifstream OpenStudentFile("parse_resume_data_to_cpp.json");

    if (!OpenCompanyFile.is_open())
    {
        cout << "Company JSON not found\n";
        return 1;
    }
    if (!OpenStudentFile.is_open())
    {
        cout << "Student JSON not found\n";
        return 1;
    }

    OpenCompanyFile >> company_data;
    OpenStudentFile >> student_data;

    Candidate candidate = parse_candidate(student_data);

    priority_queue<CompanyResult,
                   vector<CompanyResult>,
                   Compare>
        pq;

    stack<string> processed_companies;

    /* ===================== PROCESS COMPANIES ===================== */

    for (auto &comp : company_data)
    {

        vector<string> qualifications =
            comp["Qualification"].get<vector<string>>();

        if (!qualification_match(qualifications, candidate.branch))
            continue;

        vector<string> required =
            comp["Skills"].get<vector<string>>();

        vector<string> preferred =
            comp["Preferred Skills"].get<vector<string>>();

        int matched_required = 0;
        double score = calculate_score_10(
            required, preferred, candidate, matched_required);

        // Must match at least one required skill
        if (matched_required == 0)
            continue;

        CompanyResult result;
        result.company = comp["Company"];
        result.role = comp["Role"];
        result.score = score;

        // Matched skills
        for (auto &s : required)
            if (candidate.skills.count(normalize(s)))
                result.matched_skills.push_back(s);

        for (auto &s : preferred)
            if (candidate.skills.count(normalize(s)))
                result.matched_skills.push_back(s);

        // Skill gap
        for (auto &s : required)
            if (!candidate.skills.count(normalize(s)))
                result.skill_gap.push_back(s);

        for (auto &s : preferred)
            if (!candidate.skills.count(normalize(s)))
                result.skill_gap.push_back(s);

        pq.push(result);
        processed_companies.push(result.company);
    }

    /* ===================== OUTPUT ===================== */

    if (pq.empty())
    {
        cout << "No eligible companies found.\n";
        return 0;
    }

  
    json output;
    output["candidate_name"] = candidate.name;
    output["candidate_branch"] = candidate.branch;
    output["matched_companies"] = json::array();

    while (!pq.empty())
    {
        CompanyResult r = pq.top();
        pq.pop();

        json cj;
        cj["company"] = r.company;
        cj["role"] = r.role;
        cj["score"] = r.score;
        cj["matched_skills"] = r.matched_skills;
        cj["skill_gap"] = r.skill_gap;

        output["matched_companies"].push_back(cj);
    }

    ofstream out("result.json");
    out << output.dump(4);
    out.close();

    return 0;
}
