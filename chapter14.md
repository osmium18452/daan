### [1.](../programs/chapter14/14.4.1.cpp)

```c++
#include <iostream>
#include <algorithm>

#define maxn 1000
using namespace std;

int main() {
    int n, a[maxn];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n);
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    return 0;
}
```

### [2.](../programs/chapter14/14.4.2.cpp)

```c++
#include <stdio.h>
#include <string>
#include <stdlib.h>

using std::string;
using std::to_string;

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        string name = "data";
        if (i < 10) {
            name = name + "0" + to_string(i) + ".txt";
        } else {
            name = name + to_string(i) + ".txt";
        }
        freopen(name.c_str(), "r", stdin);
        int cnt = 0;
        int line = 0;
        char a;
        while ((a = getchar()) != EOF) {
            if (a == '\n') line++;
            cnt++;
        }
        printf("doc: %s, line: %d, letter: %d\n", name.c_str(), line, cnt);
    }
    return 0;
}

```

### [3.](../programs/chapter14/14.4.3.cpp)

```c++
#include <stdio.h>

int main() {
    FILE *in=fopen("in.txt","r");
    FILE *out=fopen("out.txt","a+");
    char a;
    while ((a=fgetc(in))!=EOF){
        fputc(a,out);
    }
    return 0;
}

```

### [4.](../programs/chapter14/14.4.4.cpp)

```c++
#include <stdio.h>
#include <stdlib.h>

struct node {
    int val;
    node *next;
};

void save(node *head, char *name) {
    FILE *f = fopen(name, "w");
    node *p = head;
    while (p != NULL) {
        fprintf(f, "%d ", p->val);
        p = p->next;
    }
    fclose(f);
}

node *load(char *name) {
    node *head = NULL;
    FILE *f = fopen(name, "r");
    int a;
    while (~fscanf(f, "%d", &a)) {
        node *p = (node *) malloc(sizeof(node));
        p->val = a;
        p->next = head;
        head = p;
    }
    fclose(f);
    return head;
}

int main() {
    int n, a;
    scanf("%d", &n);
    node *head = NULL;
    while (n--) {
        scanf("%d", &a);
        node *p = (node *) malloc(sizeof(node));
        p->val = a;
        p->next = head;
        head = p;
    }
    char fileName[10] = "sv.txt";
    save(head, fileName);
    node *head2 = load(fileName);
    node *p = head2;
    while (p != NULL) {
        printf("%d ", p->val);
        p = p->next;
    }
    return 0;
}

```

### [5.](../programs/chapter14/14.4.5.cpp)

```c++
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *f1 = fopen("../in1.txt", "r");
    FILE *f2 = fopen("../in2.txt", "r");
    char a[100];
    char b[100];
    printf("             in1.txt | in2.txt\n");
    printf("---------------------+---------------------\n");
    while (true) {
        bool flaga = false, flagb = false;
        if (~fscanf(f1, "%[^\n]%*c", a)) {
            flaga = true;
        }
        if (~fscanf(f2, "%[^\n]%*c", b)) {
            flagb = true;
        }
        if (flaga && flagb) {
            printf("%20s |", a);
            printf(" %-20s\n", b);
        } else if (!flagb && !flaga) {
            break;
        } else {
            if (flaga) {
                printf("%20s |\n", a);
                while (~fscanf(f1, "%[^\n]%*c", a)) {
                    printf("%20s |\n", a);
                }
                break;
            } else if (flagb) {
                printf("                     | %-20s\n", b);
                while (~fscanf(f2, "%[^\n]%*c", b)) {
                    printf("                     | %-20s\n", b);
                }
                break;
            }
        }
    }
}
```

### [6.](../programs/chapter14/14.4.6.cpp)

```c++
#include <stdio.h>

int main() {
    FILE *f = fopen("in.txt", "rb");
    char c;
    int columncnt = 0;
    printf("+------------------------------------\n| ");
    while (true) {
        c = fgetc(f);
        if (c == EOF) {
            break;
        } else {
            if (columncnt % 4 == 0 && columncnt != 0 && columncnt % 16 != 0) printf(" ");
            if (columncnt % 16 == 0 && columncnt != 0) printf("\n| ");
            printf("%02X", c);
            columncnt++;
        }
    }
    return 0;
}
```

### [7.](../programs/chapter14/14.4.7.cpp)

```c++
#include <stdio.h>

int main() {
    int a, b, c;
    char name[30], stdnum[30];
    FILE *f = fopen("out.txt", "w");
    for (int i = 0; i < 30; i++) {
        scanf("%s%s%d%d%d", stdnum, name, &a, &b, &c);
        fprintf(f, "%s %s %d %d %d\n", stdnum, name, a, b, c);
    }
    return 0;
}
```

### [8.](../programs/chapter14/14.4.8.cpp)

```c++
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct stuff {
    int salary;
    char snum[10], name[30], sex[10], birth[10], email[30];
};

struct node {
    stuff sf;
    node *next;
};

node *load(char *filename, int *n) {
    node *head = NULL;
    FILE *f = fopen(filename, "rb");
    if (fread(n, sizeof(int), 1, f) == 1) {
        for (int i = 0; i < *n; i++) {
            node *p = (node *) malloc(sizeof(stuff));
            fread(&(p->sf), sizeof(stuff), 1, f);
            p->next = head;
            head = p;
        }
    }
    return head;
}

void save(char *filename, int n, node *head) {
    FILE *f = fopen(filename, "wb");
    fwrite(&n, sizeof(int), 1, f);
    while (head != NULL) {
        fwrite(&(head->sf), sizeof(stuff), 1, f);
        head = head->next;
    }
}

void print(node *head) {
    while (head != NULL) {
        printf("worker num: %s\nname: %s\nsex: %s\nbirthday: %s\nemail: %s\nsalary: %d\n\n", head->sf.snum,
               head->sf.name, head->sf.sex, head->sf.birth, head->sf.email, head->sf.salary);
        head = head->next;
    }
}

node *add(node *head, int *n) {
    (*n)++;
    node *p = (node *) malloc(sizeof(node));
    p->next = head;
    head = p;
    scanf("%s%s%s%s%s%d", head->sf.snum, head->sf.name, head->sf.sex, head->sf.birth, head->sf.email,
          &(head->sf.salary));
    return head;
}

node *del(node *head, int *n, char *snum) {
    if (strcmp(head->sf.snum, snum) == 0) {
        (*n)--;
        head = head->next;
    } else {
        node *p = head;
        node *prev = NULL;
        while (p != NULL && strcmp(p->sf.snum, snum) != 0) {
            prev = p;
            p = p->next;
        }
        if (p != NULL) {
            (*n)--;
            prev->next = p->next;
        }
    }
    return head;
}

void find(node *head, char *snum) {
    while (head != NULL && strcmp(head->sf.snum, snum) != 0) {
        head = head->next;
    }
    if (head == NULL) printf("cannot found");
    else {
        printf("worker num: %s\nname: %s\nsex: %s\nbirthday: %s\nemail: %s\nsalary: %d\n\n", head->sf.snum,
               head->sf.name, head->sf.sex, head->sf.birth, head->sf.email, head->sf.salary);
    }
}

int main() {
    int n = 2;
    node *head = NULL;
    char *filename = "test.bin";
    head = load(filename, &n);
    while (true) {
        char instr[20];
        scanf("%s", instr);
        if (strcmp(instr, "exit") == 0) break;
        else if (strcmp(instr, "find")) {
            char snum[30];
            scanf("%s", snum);
            find(head, snum);
        } else if (strcmp(instr, "del")) {
            char snum[30];
            scanf("%s", snum);
            head = del(head,&n, snum);;
        } else if (strcmp(instr, "add")) {
            head=add(head,&n);
        } else if (strcmp(instr, "print")) {
            print(head);
        }
    }
    save(filename, n, head);
    return 0;
}

//  use the code below to make a demo
/*
    node *head = NULL;
    node *p = (node *) malloc(sizeof(stuff));
    p->next = head;
    head = p;
    p->sf.salary = 100;
    strcpy(p->sf.email, "123@qq.com");
    strcpy(p->sf.birth, "19111111");
    strcpy(p->sf.sex, "man");
    strcpy(p->sf.name, "lmao");
    strcpy(p->sf.snum, "123456");
    p = (node *) malloc(sizeof(stuff));
    p->next = head;
    head = p;
    p->sf.salary = 1000;
    strcpy(p->sf.email, "666@qq.com");
    strcpy(p->sf.birth, "19221111");
    strcpy(p->sf.sex, "woman");
    strcpy(p->sf.name, "haha");
    strcpy(p->sf.snum, "654321");
    char *filename = "test.bin";
    save(filename, n, head);
    */```

### [9.](../programs/chapter14/14.4.9.cpp)

```c++
#include <stdio.h>
#include <string.h>

int main() {
    FILE *f = fopen("in.c", "r");
    char s[100];
    int cnt = 0;
    while (~fscanf(f, "%s", s)) {
        if (strcmp(s, "int") == 0) cnt++;
        if (strcmp(s, "auto") == 0) cnt++;
        if (strcmp(s, "break") == 0) cnt++;
        if (strcmp(s, "case") == 0) cnt++;
        if (strcmp(s, "char") == 0) cnt++;
        if (strcmp(s, "const") == 0) cnt++;
        if (strcmp(s, "continue") == 0) cnt++;
        if (strcmp(s, "default") == 0) cnt++;
        if (strcmp(s, "do") == 0) cnt++;
        if (strcmp(s, "double") == 0) cnt++;
        if (strcmp(s, "else") == 0) cnt++;
        if (strcmp(s, "enum") == 0) cnt++;
        if (strcmp(s, "extern") == 0) cnt++;
        if (strcmp(s, "float") == 0) cnt++;
        if (strcmp(s, "for") == 0) cnt++;
        if (strcmp(s, "goto") == 0) cnt++;
        if (strcmp(s, "if") == 0) cnt++;
        if (strcmp(s, "long") == 0) cnt++;
        if (strcmp(s, "register") == 0) cnt++;
        if (strcmp(s, "return") == 0) cnt++;
        if (strcmp(s, "short") == 0) cnt++;
        if (strcmp(s, "signed") == 0) cnt++;
        if (strcmp(s, "sizeof") == 0) cnt++;
        if (strcmp(s, "static") == 0) cnt++;
        if (strcmp(s, "struct") == 0) cnt++;
        if (strcmp(s, "switch") == 0) cnt++;
        if (strcmp(s, "typedef") == 0) cnt++;
        if (strcmp(s, "unsigned") == 0) cnt++;
        if (strcmp(s, "union") == 0) cnt++;
        if (strcmp(s, "void") == 0) cnt++;
        if (strcmp(s, "volatile") == 0) cnt++;
        if (strcmp(s, "while") == 0) cnt++;
    }
    printf("%d", cnt);
    return 0;
}
```

### [10.](../programs/chapter14/14.4.10.cpp)

参见14.8

### [11.](../programs/chapter14/14.4.11.cpp)

```c++
//todo
```

### [12.](../programs/chapter14/14.4.12.cpp)

```c++
//todo
```

### [13.](../programs/chapter14/14.4.13.cpp)

```c++

#include <stdio.h>
#include <stdlib.h>

struct node {
    float coef;
    int exp;
    struct node *next;
};


node *CreateList(int n)
{
    node *head = (node *) malloc(sizeof(node)), *p, *pre = head;
    float coef;
    int exp;
    head->next = NULL;
    for (int i = 0; i < n; i++) {
        scanf("%f%d", &coef, &exp);
        p->coef = coef;
        p->exp = exp;
        p->next = NULL;

        pre->next = p;
        pre = p;
    }
    return head;
}

int printflist(node *head)
{
    node *p = head->next;
    while (p->next != NULL) {
        printf("%1.1f*X^%d+", p->coef, p->exp);
        p = p->next;
    }
    printf("%1.1f*X^%d\n", p->coef, p->exp);
    return 0;
}


int InverseList(node *head)
{
    node *p = head->next, *q;
    head->next = NULL;
    while (p) {
        q = p->next;
        p->next = head->next;
        head->next = p;
        p = q;
    }
    return 0;
}

node *MultiplisePoly(node *head_a, node *head_b)
{
    node *head_c, *pa = head_a, *pb = head_b, *pc, *newnode;
    int exp_max;
    if (pa->next != NULL && pb->next != NULL)
        exp_max = pa->next->exp + pb->next->exp;
    else return NULL;

    head_c = (node *) malloc(sizeof(node));
    head_c->coef = 0.0;
    head_c->exp = 0;
    head_c->next = NULL;
    pc = head_c;
    InverseList(head_b);
    float ceof = 0.0;
    for (int k = exp_max; k >= 0; k--) {
        pa = head_a->next;
        while (pa != NULL && pa->exp > k)
            pa = pa->next;
        pb = head_b->next;
        while (pa != NULL && pb != NULL && pa->exp + pb->exp < k)
            pb = pb->next;

        while (pa != NULL && pb != NULL) {
            if (k == pa->exp + pb->exp) {
                ceof += pa->coef * pb->coef;
                pa = pa->next;
                pb = pb->next;
            } else {
                if (pa->exp + pb->exp < k)
                    pb = pb->next;
                else
                    pa = pa->next;
            }

        }
        if (ceof != 0.0) {

            newnode->coef = ceof;
            newnode->exp = k;
            newnode->next = NULL;

            pc->next = newnode;
            pc = newnode;
            ceof = 0.0;
        }
    }

    InverseList(head_b);
    return head_c;
}


int main()
{
    int n;
    scanf("%d", &n);
    node *head_a = CreateList(n);
    scanf("%d", &n);
    node *head_b = CreateList(n);
    node *head_c = MultiplisePoly(head_a, head_b);
    printflist(head_c);
    return 0;
}
```

### [15.](../programs/chapter14/14.4.15.cpp)

```c++
#include <stdio.h>

int main() {
    char s[1000];
    int stack_ele_num = 0;
    scanf("%s", s);
    int i = 0;
    while (s[i] == 'I' || s[i] == 'O') {
        if (s[i] == 'I') stack_ele_num++;
        else {
            if (stack_ele_num > 0) stack_ele_num--;
            else {
                printf("illegal i/o");
                return 0;
            }
        }
        i++;
    }
    printf("legal i/o");
    return 0;
}
```

### [16.](../programs/chapter14/14.4.16.cpp)

```c++
#include <stdio.h>

#define maxn 10000
char stack[maxn];

int main() {
    char s[maxn * 10];
    int top = 0;
    scanf("%s", s);
    int i = 0;
    while (s[i] != '\0') {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[top++] = s[i];
        } else if (s[i] == ')' || s[i] == ']' || s[i] == '}') {
            if ((stack[top - 1] == '(' && s[i] == ')') || (stack[top - 1] == '[' && s[i] == ']') ||
                (stack[top - 1] == '{' && s[i] == '}')) {
                top--;
            } else {
                printf("braces mismatch");
                return 0;
            }
        }
        i++;
    }
    printf("braces match");
    return 0;
}
```

### [17.](../programs/chapter14/14.4.17.cpp)

```c++
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define ERROR -1
#define TRUE 1
#define OK 0
#define STACK_INIT_SIZE 30
#define STACKINCREMENT 50
struct stack {
    int *bottom;
    int *top;
    int stacksize;
};

int InitStack(stack &S) {
S.bottom = (int *) malloc(STACK_INIT_SIZE
                          * sizeof(char));
if (!S.bottom) exit(OVERFLOW);
S.
top = S.bottom;
S.
stacksize = STACK_INIT_SIZE;
return OK;
}

int push(stack &S, int ch) {
if (S.top - S.bottom >= S.stacksize) {
S.bottom = (int *) realloc(S.bottom, S.stacksize + STACKINCREMENT * sizeof(int));
if (!S.bottom) exit(OVERFLOW);
S.top = S.bottom + S.stacksize;
S.stacksize += STACKINCREMENT;
}
*S.top = ch;
S.top = S.top + 1;
return OK;
}

int pop(stack &S, int &ch) {
if (S.top == S.bottom) return ERROR;
ch = *(S.top - 1);
S.top--;
*(S.top) = 0;
return OK;
}

int GetTop(stack &S) {
int ch;
if (S.top == S.bottom) return ERROR;
ch = *(S.top - 1);
return ch;
}

int IsOptr(char ch) {
    int i = 0;
    char optr[] = {'+', '-', '*', '/', '(', ')', '#', '@'};
    while (optr[i] != '@') {
        if (ch == optr[i]) return TRUE;
        i++;
    }
    return OK;
}

char Precede(int sym1, int sym2) {
    if (sym1 == '#' && sym2 == '#') return '=';
    else if (sym1 == '#' && sym2 == ')') exit(ERROR);
    else if (sym1 == '#') return '<';
    else if (sym1 == '(' && sym2 == '#') exit(ERROR);
    else if (sym2 == '#') return '>';
    else if (sym1 == ')' && sym2 == '(') exit(ERROR);
    else if (sym1 == ')') return '>';
    else if (sym1 == '(' && sym2 == ')') return '=';
    else if (sym2 == ')') return '>';
    else if (sym1 == '(') return '<';
    else if (sym2 == '(') return '<';
    else if (sym1 == '*' || sym1 == '/' || sym2 == '+' || sym2 == '-') return '>';
    else return '<';
}

int Operate(int a, int theta, int b) {
    if (theta == '+') return a + b;
    else if (theta == '-') return a - b;
    else if (theta == '*') return a * b;
    else if (theta == '/') {
        if (b == 0) {
            printf("该行除数为0，出错！");
            return NULL;
        } else return a / b;
    } else exit(ERROR);
}

FILE *fp;

int main() {
    stack OPTR, OPND;
    char c = '0';
    int x, theta, a, b;
    fp = fopen("../in.txt", "r");
    while (c != EOF) {
        InitStack(OPTR);
        push(OPTR, '#');
        InitStack(OPND);
        c = fgetc(fp);
        while (c != '#' || GetTop(OPTR) != '#') {
            if (!IsOptr(c)) {
                push(OPND, c - 48);
                c = fgetc(fp);
                while (!IsOptr(c)) {
                    pop(OPND, x);
                    push(OPND, x * 10 + c - 48);
                    c = fgetc(fp);
                }
            } else
                switch (Precede(GetTop(OPTR), c)) {
                    case '<':
                        push(OPTR, c);
                        c = fgetc(fp);
                        break;
                    case '=':
                        pop(OPTR, x);
                        c = fgetc(fp);
                        break;
                    case '>':
                        pop(OPTR, theta);
                        pop(OPND, b);
                        pop(OPND, a);
                        push(OPND, Operate(a, theta, b));
                        break;
                }
        }
        printf("%d\n", GetTop(OPND));
        c = fgetc(fp);
    }
    fclose(fp);
    return 0;
}


```

### [18.](../programs/chapter14/14.4.18.cpp)

```c++
#include <stdio.h>
#include <string.h>

int main() {
    char s[] = {'A', 'B', 'C', 'D'};
    int top = 0;
    int train = 0;
    int stack[4];
    char c[10];
    for (int i = 0; i < 8; i++) {
        scanf("%s", c);
        if (strcmp(c, "in") == 0) {
            stack[top++] = s[train++];
        } else if (strcmp(c, "out") == 0) {
            if (top > 0) {
                printf("train %c out\n", stack[--top]);
            } else {
                printf("no train in station\n");
                return 0;
            }
        } else {
            printf("type in \"in\" or \"out\"\n");
        }
    }
    return 0;
}
```

### [19.](../programs/chapter14/14.4.19.cpp)

```c++

#include <stdio.h>
#include <stdlib.h>

struct node {
    int no;
    node *next;
};

int main() {
    int n, m, s;
    scanf("%d%d%d", &n, &s, &m);
    if (m == 0) {
        for (int i = 1; i <= n; i++) {
            printf("%d ", i);
        }
        return 0;
    }
    node *head = NULL, *tail;
    for (int i = 0; i < n; i++) {
        node *p = (node *) malloc(sizeof(node));
        p->no = n - i;
        p->next = head;
        head = p;
        if (i == 0) tail = p;
    }
    tail->next = head;
    node *p = head, *prev = NULL;
    for (int i = 1; i < s; i++) p = p->next;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < m; j++) {
            prev = p;
            p = p->next;
        }
        prev->next = p->next;
        printf("%d ", p->no);
        free(p);
        p = prev->next;
    }
    return 0;
}
```

### [20.](../programs/chapter14/14.4.20.cpp)

```c++

#include <stdio.h>
#include <string.h>

#define maxn 1000
int map[maxn][maxn];
int visited[maxn][maxn];
int queuex[maxn * 10], queuey[maxn * 10];
int prev[maxn * 10];
int path[maxn * 10];

int main() {
    int m, n;
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &map[i][j]);
        }
    }
    memset(visited, 0, sizeof(visited));
    int x1, y1, x2, y2;
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    int h = 0, t = 0;
    queuex[t] = x1;
    queuey[t++] = y1;
    visited[x1][y1] = true;
    bool found = false;
    while (h != t) {
        int x = queuex[h], y = queuey[h++];
        if (x == x2 && y == y2) {
            int cnt = 0;
            int i = h - 1;
            path[cnt++] = i;
            while (i != 0) {
                i = prev[i];
                path[cnt++] = i;
            }
            found = true;
            while (cnt--) {
                printf("(%d, %d) ", queuex[path[cnt]], queuey[path[cnt]]);
            }
            break;
        }
        if (x + 1 < n && !visited[x + 1][y] && map[x + 1][y] == 0) {
            queuex[t] = x + 1;
            queuey[t] = y;
            prev[t++] = h - 1;
            visited[x + 1][y] = true;
        }
        if (x - 1 >= 0 && !visited[x - 1][y] && map[x - 1][y] == 0) {
            queuex[t] = x - 1;
            queuey[t] = y;
            prev[t++] = h - 1;
            visited[x - 1][y] = true;
        }
        if (y + 1 < m && !visited[x][y + 1] && map[x][y + 1] == 0) {
            queuex[t] = x;
            queuey[t] = y + 1;
            prev[t++] = h - 1;
            visited[x][y + 1] = true;
        }
        if (y - 1 >= 0 && !visited[x][y - 1] && map[x][y - 1] == 0) {
            queuex[t] = x;
            queuey[t] = y - 1;
            prev[t++] = h - 1;
            visited[x][y - 1] = true;
        }
    }
    if (!found) printf("path not found");
    return 0;
}

/*
3 3
0 0 0
1 1 0
1 1 0
0 0 2 2
 */
```

