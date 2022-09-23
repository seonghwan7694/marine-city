# 👩🏾‍🏫 source_code Information

###### 📣 추가하고 싶은 아두이노 파일이 있다면, '파일 이름'과 '기능에 대한 설명'을 이슈 탭에 올려주세요. 아니면 [풀 리퀘스트](https://seungwubaek.github.io/tools/git/contributing_using_pull_request/)를 해주세요.

| Order 	|       Name      	| Code 	| 작성자(책임자) 	|              기능에 대한 간단한 설명              	|
|:-----:	|:---------------:	|:----:	|:--------------:	|:-------------------------------------------------:	|
|   1   	|                 	|      	|                	|  중앙 서버 역할을 할 라즈베리파이를 위해 비워둠.  	|
|   2   	|  NodeMCU_1.ino  	|   [💾💾💾](NodeMCU_1.ino)   	|        김성환      	| 이 MCU는 RBP 3에 의해 제어되며 A 기능을 구현했다. 	|
|   3   	|  NodeMCU_2.ino  	|   [💾💾💾](NodeMCU_2.ino)   	|        김준형        	| 이 MCU는 RBP 3에 의해 제어되며 B 기능을 구현했다. 	|
|   4   	|  NodeMCU_3.ino  	|   [💾💾💾](NodeMCU_3.ino)  	|        김호성        	| 이 MCU는 RBP 3에 의해 제어되며 C 기능을 구현했다. 	|
|   5   	|  NodeMCU_4.ino  	|   [💾💾💾](NodeMCU_4.ino)   	|        이민형        	| 이 MCU는 RBP 3에 의해 제어되며 D 기능을 구현했다. 	|
|   6   	|  motor_test.ino 	|   [💾💾💾](motor_test.ino)   	|                	|      모터가 정상적으로 작동하는지 확인하는 곳     	|
|   7   	| sensor_test.ino 	|   [💾💾💾](sensor_test.ino)   	|                	|      센서가 정상적으로 작동하는지 확인하는 곳     	|
|   8   	|      *.ino      	|      	|                	|             추후에 추가될 예정입니다.             	|

# 👨🏻‍💻 [Recommended C style and coding rules - Reference](https://github.com/MaJerle/c-code-style#the-single-most-important-rule)

## Table of Contents

  - [The single most important rule](##the-single-most-important-rule)
  - [General rules](##general-rules)
  - [Comments](##comments)
  - [Functions](##functions)
  - [Variables](##variables)
  - [Structures, enumerations, typedefs](##structures-enumerations-typedefs)
  - [Compound statements](##compound-statements)
    - [Switch statement](##switch-statement)

## The single most important rule

Let's start with the quote from [GNOME developer](https://developer.gnome.org/programming-guidelines/stable/c-coding-style.html.en) site.

> The single most important rule when writing code is this: *check the surrounding code and try to imitate it*.
>
> As a maintainer it is dismaying to receive a patch that is obviously in a different coding style to the surrounding code. This is disrespectful, like someone tromping into a spotlessly-clean house with muddy shoes.
>
> So, whatever this document recommends, if there is already written code and you are patching it, keep its current style consistent even if it is not your favorite style.

## General rules

Here are listed most obvious and important general rules. Please check them carefully before you continue with other chapters.

- Use `C99` standard
- Do not use tabs, use spaces instead
- Use `2` spaces per indent level
- Use `1` space between keyword and opening bracket
```c
/* OK */
if (condition)
while (condition)
for (init; condition; step)
do {} while (condition)

/* Wrong */
if(condition)
while(condition)
for(init;condition;step)
do {} while(condition)
```

- Do not use space between function name and opening bracket
```c
int32_t a = sum(4, 3);              /* OK */
int32_t a = sum (4, 3);             /* Wrong */
```

- Never use `__` or `_` prefix for variables/functions/macros/types. This is reserved for C language itself
    - Prefer `prv_` name prefix for strictly module-private functions
- Use only lowercase characters for variables/functions/macros/types with optional underscore `_` char
- Opening curly bracket is always at the same line as keyword (`for`, `while`, `do`, `switch`, `if`, ...)
```c
size_t i;
for (i = 0; i < 5; ++i) {           /* OK */
}
for (i = 0; i < 5; ++i){            /* Wrong */
}
for (i = 0; i < 5; ++i)             /* Wrong */
{
}
```

- Use single space before and after comparison and assignment operators
```c
int32_t a;
a = 3 + 4;              /* OK */
for (a = 0; a < 5; ++a) /* OK */
a=3+4;                  /* Wrong */
a = 3+4;                /* Wrong */
for (a=0;a<5;++a)       /* Wrong */
```

- Use single space after every comma
```c
func_name(5, 4);        /* OK */
func_name(4,3);         /* Wrong */
```

- Do not initialize `static` and `global` variables to `0` (or `NULL`), let compiler do it for you. Do not use 'static' storage class.
```c
static int32_t a;       /* OK */
static int32_t b = 4;   /* OK */
static int32_t a = 0;   /* Wrong */

void my_func(void) {
    static int32_t* ptr;/* OK */
    static char abc = 0;/* Wrong */
}
```

- Declare all local/global variables of the same functionality in the same line or the same paragraph.
```c
void
my_func(void) {

    char char_variable_for_func_a;             /* OK */
    int int_variable_for_func_a;

    char char_variable_for_func_b, char_variable_for_func_c;          /* Wrong, these variable does not have the same functionally*/
    int int_variable_for_func_d;

}
```

- Declare local variables in order
    1. Custom structures and enumerations
    2. Integer types, wider unsigned type first
    3. Single/Double floating point
```c
int
my_func(void) {
    /* 1 */
    my_struct_t my;     /* First custom structures */
    my_struct_ptr_t* p; /* Pointers too */

    /* 2 */
    uint32_t a;
    int32_t b;
    uint16_t c;
    int16_t g;
    char h;
    /* ... */

    /* 3 */
    double d;
    float f;
}
```

- Always declare local variables at the beginning of the block, before first executable statement

- Declare counter variables in `for` loop
```c
/* OK */
for (size_t i = 0; i < 10; ++i)

/* OK, if you need counter variable later */
size_t i;
for (i = 0; i < 10; ++i) {
    if (...) {
        break;
    }
}
if (i == 10) {

}

/* Wrong, if you don't need counter variable later */
size_t i;
for (i = 0; i < 10; ++i) ...
```

- Avoid variable assignment with function call in declaration, except for single variables
```c
void a(void) {
    /* Avoid function calls when declaring variable */
    int32_t a, b = sum(1, 2);

    /* Use this */
    int32_t a, b;
    b = sum(1, 2);

    /* This is ok */
    uint8_t a = 3, b = 4;
}
```

- Except `char`, `float` or `double`, always use types declared in `stdint.h` library, eg. `uint8_t` for `unsigned 8-bit`, etc.
- Do not use `stdbool.h` library. Use `1` or `0` for `true` or `false` respectively
```c
/* OK */
uint8_t status;
status = 0;

/* Wrong */
#include <stdbool.h>
bool status = true;
```

- Never compare against `true`, eg. `if (check_func() == 1)`, use `if (check_func()) { ... }`
- Always compare pointers against `NULL` value
```c
void* ptr;

/* ... */

/* OK, compare against NULL */
if (ptr == NULL || ptr != NULL) {

}

/* Wrong */
if (ptr || !ptr) {

}
```

- Always use *pre-increment (and decrement respectively)* instead of *post-increment (and decrement respectively)*
```c
int32_t a = 0;
...

a++;            /* Wrong */
++a;            /* OK */

for (size_t j = 0; j < 10; ++j) {}  /* OK */
```

- Always use `size_t` for length or size variables
- Always use `const` for pointer if function should not modify memory pointed to by `pointer`
- Always use `const` for function parameter or variable, if it should not be modified
```c

/* When d could be modified, data pointed to by d could not be modified */
void my_func(const void* d) {

}

/* When d and data pointed to by d both could not be modified */
void my_func(const void* const d) {

}

/* Not required, it is advised */
void my_func(const size_t len) {

}

/* When d should not be modified inside function, only data pointed to by d could be modified */
void my_func(void* const d) {

}
```

- When function may accept pointer of any type, always use `void *`, do not use `uint8_t *`
    - Function must take care of proper casting in implementation
```c
/*
 * To send data, function should not modify memory pointed to by `data` variable
 * thus `const` keyword is important
 *
 * To send generic data (or to write them to file)
 * any type may be passed for data,
 * thus use `void *`
 */
/* OK example */
void send_data(const void* data, size_t len) { /* OK */
    /* Do not cast `void *` or `const void *` */
    const uint8_t* d = data;/* Function handles proper type for internal usage */
}

void send_data(const void* data, int len) {    /* Wrong, not not use int */
}
```

- Always use brackets with `sizeof` operator
```c
/* OK */
#include <stdlib.h>
void my_func(size_t size) {
    int32_t* arr;
    arr = malloc(sizeof(*arr) * n); /* OK, Allocate memory */
    arr = malloc(sizeof *arr * n);  /* Wrong, brackets for sizeof operator are missing */
    if (arr == NULL) {
        /* FAIL, no memory */
    }

    free(arr);  /* Free memory after usage */
}
```

- Always compare variable against zero, except if it is treated as `boolean` type
- Never compare `boolean-treated` variables against zero or one. Use NOT (`!`) instead
```c
size_t length = 5;  /* Counter variable */
uint8_t is_ok = 0;  /* Boolean-treated variable */
if (length)         /* Wrong, length is not treated as boolean */
if (length > 0)     /* OK, length is treated as counter variable containing multi values, not only 0 or 1 */
if (length == 0)    /* OK, length is treated as counter variable containing multi values, not only 0 or 1 */

if (is_ok)          /* OK, variable is treated as boolean */
if (!is_ok)         /* OK, -||- */
if (is_ok == 1)     /* Wrong, never compare boolean variable against 1! */
if (is_ok == 0)     /* Wrong, use ! for negative check */
```

- Always use `/* comment */` for comments, even for *single-line* comment
- Always include check for `C++` with `extern` keyword in header file
- Every function must include *doxygen-enabled* comment, even if function is `static`
- Use English names/text for functions, variables, comments
- Use *lowercase* characters for variables
- Use *underscore* if variable contains multiple names, eg. `force_redraw`. Do not use `forceRedraw`
- Never cast function returning `void *`, eg. `uint8_t* ptr = (uint8_t *)func_returning_void_ptr();` as `void *` is safely promoted to any other pointer type
    - Use `uint8_t* ptr = func_returning_void_ptr();` instead
- Always use `<` and `>` for C Standard Library include files, eg. `#include <stdlib.h>`
- Always use `""` for custom libraries, eg. `#include "my_library.h"`
- When casting to pointer type, always align asterisk to type, eg. `uint8_t* t = (uint8_t*)var_width_diff_type`
- Always respect code style already used in project or library

## Comments

- Comments starting with `//` are not allowed. Always use `/* comment */`, even for single-line comment
```c
//This is comment (wrong)
/* This is comment (ok) */
```

- For multi-line comments use `space+asterisk` for every line
```c
/*
 * This is multi-line comments,
 * written in 2 lines (ok)
 */

/**
 * Wrong, use double-asterisk only for doxygen documentation
 */

/*
* Single line comment without space before asterisk (wrong)
*/

/*
 * Single line comment in multi-line configuration (wrong)
 */

/* Single line comment (ok) */
```

- Use `12` indents (`12 * 4` spaces) offset when commenting. If statement is larger than `12` indents, make comment `4-spaces` aligned (examples below) to next available indent
```c
void my_func(void) {
    char a, b;

    a = call_func_returning_char_a(a);          /* This is comment with 12*4 spaces indent from beginning of line */
    b = call_func_returning_char_a_but_func_name_is_very_long(a);   /* This is comment, aligned to 4-spaces indent */
}
```

## Functions

- Every function which may have access from outside its module, must include function *prototype* (or *declaration*)
- Function name must be lowercase, optionally separated with underscore `_` character
```c
/* OK */
void my_func(void);
void myfunc(void);

/* Wrong */
void MYFunc(void);
void myFunc();
```

- When function returns pointer, align asterisk to return type
```c
/* OK */
const char* my_func(void);
my_struct_t* my_func(int32_t a, int32_t b);

/* Wrong */
const char *my_func(void);
my_struct_t * my_func(void);
```
- Align all function prototypes (with the same/similar functionality) for better readability
```c
/* OK, function names aligned */
void        set(int32_t a);
my_type_t   get(void);
my_ptr_t*   get_ptr(void);

/* Wrong */
void set(int32_t a);
const char * get(void);
```

## Variables

- Make variable name all lowercase with optional underscore `_` character
```c
/* OK */
int32_t a;
int32_t my_var;
int32_t myvar;

/* Wrong */
int32_t A;
int32_t myVar;
int32_t MYVar;
```

- (optionally) Group local variables together by `type`
```c
void
foo(void) {
    int32_t a, b;   /* OK */
    char a;
    char b;         /* Wrong, char type already exists */
}
```

- Do not declare variable after first executable statement
```c
void
foo(void) {
    int32_t a;
    a = bar();
    int32_t b;      /* Wrong, there is already executable statement */
}
```

- You may declare new variables inside next indent level
```c
int32_t a, b;
a = foo();
if (a) {
    int32_t c, d;   /* OK, c and d are in if-statement scope */
    c = foo();
    int32_t e;      /* Wrong, there was already executable statement inside block */
}
```

- Declare pointer variables with asterisk aligned to type
```c
/* OK */
char* a;

/* Wrong */
char *a;
char * a;
```

- When declaring multiple pointer variables, you may declare them with asterisk aligned to variable name
```c
/* OK */
char *p, *n;
```

## Structures, enumerations, typedefs

- Structure or enumeration name must be lowercase with optional underscore `_` character between words
- Structure or enumeration may contain `typedef` keyword
- All structure members must be lowercase
- All enumeration members must be uppercase

When structure is declared, it may use one of `3` different options:

1. When structure is declared with *name only*, it *must not* contain `_t` suffix after its name.
```c
struct struct_name {
    char* a;
    char b;
};
```
2. When structure is declared with *typedef only*, it *has to* contain `_t` suffix after its name.
```c
typedef struct {
    char* a;
    char b;
} struct_name_t;
```
3. When structure is declared with *name and typedef*, it *must not* contain `_t` for basic name and it *has to* contain `_t` suffix after its name for typedef part.
```c
typedef struct struct_name {
    char* a;
    char b;
    char c;
} struct_name_t;
```

Examples of bad declarations and their suggested corrections
```c
/* a and b must be separated to 2 lines */
/* Name of structure with typedef must include _t suffix */
typedef struct {
    int32_t a, b;
} a;

/* Corrected version */
typedef struct {
    int32_t a;
    int32_t b;
} a_t;

/* Wrong name, it must not include _t suffix */
struct name_t {
    int32_t a;
    int32_t b;
};

/* Wrong parameters, must be all uppercase */
typedef enum {
    MY_ENUM_TESTA,
    my_enum_testb,
} my_enum_t;
```

- When initializing structure on declaration, use `C99` initialization style
```c
/* OK */
a_t a = {
    .a = 4,
    .b = 5,
};

/* Wrong */
a_t a = {1, 2};
```

- When new typedef is introduced for function handles, use `_fn` suffix
```c
/* Function accepts 2 parameters and returns uint8_t */
/* Name of typedef has `_fn` suffix */
typedef uint8_t (*my_func_typedef_fn)(uint8_t p1, const char* p2);
```

## Compound statements

- Every compound statement must include opening and closing curly bracket, even if it includes only `1` nested statement
- Every compound statement must include single indent; when nesting statements, include `1` indent size for each nest
```c
/* OK */
if (c) {
    do_a();
} else {
    do_b();
}

/* Wrong */
if (c)
    do_a();
else
    do_b();

/* Wrong */
if (c) do_a();
else do_b();
```

- In case of `if` or `if-else-if` statement, `else` must be in the same line as closing bracket of first statement
```c
/* OK */
if (a) {

} else if (b) {

} else {

}

/* Wrong */
if (a) {

}
else {

}

/* Wrong */
if (a) {

}
else
{

}
```

- In case of `do-while` statement, `while` part must be in the same line as closing bracket of `do` part
```c
/* OK */
do {
    int32_t a;
    a = do_a();
    do_b(a);
} while (check());

/* Wrong */
do
{
/* ... */
} while (check());

/* Wrong */
do {
/* ... */
}
while (check());
```

- Indentation is required for every opening bracket
```c
if (a) {
    do_a();
} else {
    do_b();
    if (c) {
        do_c();
    }
}
```

- Never do compound statement without curly bracket, even in case of single statement. Examples below show bad practices
```c
if (a) do_b();
else do_c();

if (a) do_a(); else do_b();
```

- Empty `while`, `do-while` or `for` loops must include brackets
```c
/* OK */
while (is_register_bit_set()) {}

/* Wrong */
while (is_register_bit_set());
while (is_register_bit_set()) { }
while (is_register_bit_set()) {
}
```

- If `while` (or `for`, `do-while`, etc) is empty (it can be the case in embedded programming), use empty single-line brackets
```c
/* Wait for bit to be set in embedded hardware unit
uint32_t* addr = HW_PERIPH_REGISTER_ADDR;

/* Wait bit 13 to be ready */
while (*addr & (1 << 13)) {}        /* OK, empty loop contains no spaces inside curly brackets */
while (*addr & (1 << 13)) { }       /* Wrong */
while (*addr & (1 << 13)) {         /* Wrong */

}
while (*addr & (1 << 13));          /* Wrong, curly brackets are missing. Can lead to compiler warnings or unintentional bugs */
```
- Always prefer using loops in this order: `for`, `while`, `do-while`
- Avoid incrementing variables inside loop block if possible, see examples

```c
/* Not recommended */
int32_t a = 0;
while (a < 10) {
    .
    ..
    ...
    ++a;
}

/* Better */
for (size_t a = 0; a < 10; ++a) {

}

/* Better, if inc may not happen in every cycle */
for (size_t a = 0; a < 10; ) {
    if (...) {
        ++a;
    }
}
```

### Switch statement

- Add *single indent* for every `case` statement
- Use additional *single indent* for `break` statement in each `case` or `default`
```c
/* OK, every case has single indent */
/* OK, every break has additional indent */
switch (check()) {
    case 0:
        do_a();
        break;
    case 1:
        do_b();
        break;
    default:
        break;
}

/* Wrong, case indent missing */
switch (check()) {
case 0:
    do_a();
    break;
case 1:
    do_b();
    break;
default:
    break;
}

/* Wrong */
switch (check()) {
    case 0:
        do_a();
    break;      /* Wrong, break must have indent as it is under case */
    case 1:
    do_b();     /* Wrong, indent under case is missing */
    break;
    default:
        break;
}
```

- Always include `default` statement
```c
/* OK */
switch (var) {
    case 0:
        do_job();
        break;
    default:
        break;
}

/* Wrong, default is missing */
switch (var) {
    case 0:
        do_job();
        break;
}
```

- If local variables are required, use curly brackets and put `break` statement inside.
    - Put opening curly bracket in the same line as `case` statement
```c
switch (a) {
    /* OK */
    case 0: {
        int32_t a, b;
        char c;
        a = 5;
        /* ... */
        break;
    }

    /* Wrong */
    case 1:
    {
        int32_t a;
        break;
    }

    /* Wrong, break shall be inside */
    case 2: {
        int32_t a;
    }
    break;
}
```

