class Person{
    public:
    string name;
    int age;
    virtual void getdata() {        cin >> this->name >> this->age;    }
    virtual void putdata() {        cout << this->name << " " << this->age << endl;    }
};

class Professor: public Person{
    public:
    static int id;
    Professor() {        this->cur_id = ++id;    }
    int publications, cur_id;
    void getdata(){cin >> this->name >> this->age >> this->publications;}
    void putdata(){cout << this->name << " " << this->age << " " << this->publications << " " << this->cur_id << " " << endl;}
}; 
int Professor::id = 0;

class Student: public Person{
    #define TAMANNO 6
    public:
    int marks[TAMANNO];
    int cur_id;
    static int id;
    Student(){ this->cur_id= ++id; }
    void getdata(){
        cin >> this->name >> this->age;
        for (int i=0; i<TAMANNO; i++) { cin >> marks[i]; }
    }
    void putdata() {
        int result=0;
        for (int i=0; i<TAMANNO; i++) { result += marks[i];}
        cout << this->name << " " << this->age << " " << result << " " << this->cur_id << endl;
    }
};
int Student::id = 0;
