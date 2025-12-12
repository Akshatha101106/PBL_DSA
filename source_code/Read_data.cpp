#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <regex>
#include <fstream>

using namespace std;

double company_cutoff = 7.25; // TODO: dynamic in next update


string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}

class Student {
public:
    string name;
    string email;
    string phone;
    string linkedin_id;
    stack<string> skills;
    stack<string> education_details;
    double cgpa = 0.0;

    void printData() {
        cout << "\n----- Extracted Student Data -----\n";
        cout << "Name      : " << name << endl;
        cout << "Email     : " << email << endl;
        cout << "Phone     : " << phone << endl;
        cout << "LinkedIn  : " << linkedin_id << endl;
        cout << "CGPA      : " << cgpa << endl;

        cout << "\nSkills (Top -> Bottom): ";
        stack<string> temp1 = skills;
        while (!temp1.empty()) {
            cout << temp1.top() << ", ";
            temp1.pop();
        }

        cout << "\nEducation (Top -> Bottom): ";
        stack<string> temp2 = education_details;
        while (!temp2.empty()) {
            cout << temp2.top() << " | ";
            temp2.pop();
        }

        cout << "\n----------------------------------\n";
    }
};

/* ============================
      TXT FILE READER
   ============================ */
string readTextFile(const string &filepath) {
    ifstream in(filepath);
    if (!in) {
        cout << "\nERROR: Could not open text file.\n";
        return "";
    }

    string text = "", line;
    while (getline(in, line)) {
        text += line + "\n";
    }
    return text;
}

/* ============================
      EXTRACTORS
   ============================ */

// Name = first non-empty line
string extractName(const vector<string>& resume) {
    for (auto &line : resume)
        if (line.length() > 2) return line;
    return "Not Found";
}
// Email
string extractEmail(const string& text) {
    regex r(R"(([\w\.-]+@[\w\.-]+\.\w+))");
    smatch m;
    if (regex_search(text, m, r)) return m.str(0);
    return "Not Found";
}

// Phone
string extractPhone(const string& text) {
    regex r(R"((\+?\d{10,13}))");
    smatch m;
    if (regex_search(text, m, r)) return m.str(0);
    return "Not Found";
}

// LinkedIn
string extractLinkedIn(const string& text) {
    regex r(R"((https?:\/\/(www\.)?linkedin\.com\/[A-Za-z0-9\/\-\_\.]+))");
    smatch m;
    if (regex_search(text, m, r)) return m.str(0);
    return "Not Found";
}

// CGPA
double extractCGPA(const string& text) {
    regex r(R"((\b[0-9]\.[0-9]{1,2}\b))");
    smatch m;
    if (regex_search(text, m, r)) {
        double v = stod(m.str(0));
        if (v <= 10.0) return v;
    }
    return 0.0;
}

// CGPA cutoff
bool is_cgpa_cutoff_passed(double studentCGPA, double cutoff) {
    return studentCGPA >= cutoff;
}

// Skills database
vector<string> skillDB = {
    "c", "c++", "python", "java", "html", "css",
    "javascript", "sql", "machine learning", "computer vision",
    "data structures", "algorithms"
};

// Skill extraction
vector<string> extractSkills(const string& text) {
    vector<string> found;
    string low = toLower(text);

    for (auto &skill : skillDB) {
        if (low.find(toLower(skill)) != string::npos)
            found.push_back(skill);
    }
    return found;
}

// Education extraction
vector<string> extractEducation(const vector<string>& lines) {
    vector<string> edu;
    vector<string> keywords = {
        "b.tech", "btech", "be", "b.e", "engineering",
        "puc", "12th", "10th", "sslc", "diploma",
        "school", "college", "university"
    };

    for (auto &line : lines) {
        string low = toLower(line);
        for (auto &key : keywords) {
            if (low.find(key) != string::npos) {
                edu.push_back(line);
                break;
            }
        }
    }
    return edu;
}
/* ============================
           MAIN
   ============================ */
int main() {
    queue<Student> studentQueue;

    cout << "===== Resume Extraction System (.txt version) =====\n";
    cout << "Enter Resume .txt file path:\n";

    string txtPath;
    getline(cin, txtPath);

    string fullText = readTextFile(txtPath);

    if (fullText.empty()) {
        cout << "Error: Could not read text from file.\n";
        return 1;
    }

    // Convert text → vector<string> (line by line)
    vector<string> resumeLines;
    string temp = "";
    for (char c : fullText) {
        if (c == '\n') {
            resumeLines.push_back(temp);
            temp = "";
        } else temp += c;
    }

    Student s;

    s.name = extractName(resumeLines);
    s.email = extractEmail(fullText);
    s.phone = extractPhone(fullText);
    s.linkedin_id = extractLinkedIn(fullText);
    s.cgpa = extractCGPA(fullText);

    for (auto &sk : extractSkills(fullText))
        s.skills.push(sk);

    for (auto &ed : extractEducation(resumeLines))
        s.education_details.push(ed);

    studentQueue.push(s);

    cout << "\nStudent data extracted successfully.\n";

    Student stored = studentQueue.front();
    stored.printData();

    if (is_cgpa_cutoff_passed(stored.cgpa, company_cutoff))
        cout << "\nCGPA meets cutoff!\n";
    else
        cout << "\nCGPA does NOT meet cutoff.\n";

    return 0;
}