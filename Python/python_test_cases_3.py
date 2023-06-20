"""
Program_3_Test_Cases:
Lines of Code : 87
Number of Test Cases : 5
Test Cases include:
    •Input :10
            6 10
            ........**
            .**......*
            ..*..*....
            .....**...
            ...*.....*
            ..**....**
            6 10
            ....*...**
            .**......*
            ..*..*....
            .....**...
            ...*.....*
            ..**....**
            3 3
            ...
            ***
            ...
            4 4
            .*..
            **..
            ..**
            ..*.
            5 4
            .*..
            **..
            ....
            ..**
            ..*.
            3 2
            .*
            **
            *.
            2 3
            *..
            .**
            3 2
            ..
            **
            *.
            3 3
            .**
            *.*
            **.
            3 3
            ..*
            .**
            ..*
     Output:YES
            NO
            NO
            NO
            YES
            NO
            NO
            YES
            NO
            NO
    
    •Input :100
            3 2
            **
            **
            **
            2 3
            .**
            ***
            3 2
            *.
            **
            **
            2 3
            ..*
            ***
            3 2
            **
            .*
            **
            2 3
            .*.
            ***
            2 3
            *..
            ***
            2 3
            ...
            ***
            2 3
            ***
            .**
            3 2
            .*
            *.
            **
            2 3
            *.*
            .**
            2 3
            ..*
            .**
            3 2
            **
            ..
            **
            3 2
            .*
            ..
            **
            2 3
            *..
            .**
            3 2
            ..
            ..
            **
            3 2
            **
            **
            .*
            3 2
            .*
            **
            .*
            3 2
            *.
            **
            .*
            2 3
            ..*
            *.*
            2 3
            **.
            *.*
            2 3
            .*.
            *.*
            3 2
            *.
            .*
            .*
            2 3
            ...
            *.*
            2 3
            ***
            ..*
            3 2
            .*
            *.
            .*
            3 2
            *.
            *.
            .*
            3 2
            ..
            *.
            .*
            3 2
            **
            ..
            .*
            3 2
            .*
            ..
            .*
            3 2
            *.
            ..
            .*
            2 3
            .....
     Output:NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES

    •Input : 100
            50 50
            ..................................................
            ............**..............................*.....
            ............*..............................**.....
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ...............................*..................
            ..............................**...*..............
            ..................................
     Output:NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            YES
            YES
            YES
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            YES
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            YES
            NO
            NO
            NO
            YES
            YES
            NO
            NO
            NO
            NO
            NO
            YES
            YES
            YES
            NO
            NO
            YES
            NO
            YES
            NO
            NO
            YES
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            YES
            YES
            NO
            NO
            YES
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
     
    •Input : 100
            3 3
            .*.
            ..*
            *..
            3 3
            **.
            .*.
            .*.
            3 3
            ***
            ..*
            *.*
            3 3
            *..
            .*.
            ***
            3 3
            *..
            ***
            ...
            3 3
            .**
            ...
            ..*
            3 3
            **.
            ...
            .*.
            3 3
            *.*
            *.*
            ***
            3 3
            .**
            *.*
            .*.
            3 3
            .**
            ...
            ...
            3 3
            **.
            ***
            .*.
            3 3
            *.*
            ...
            .**
            3 3
            *..
            .*.
            *..
            3 3
            *.*
            *..
            .**
            3 3
            *..
            **.
            ...
            3 3
            .**
            **.
            .**
            3 3
            *..
            *..
            *..
            3 3
            .*.
            *..
            *..
            3 3
            ***
            ***
            *..
            3 3
            .**
            *.*
            ..*
            3 3
            ***
            *..
            **.
            3 3
            ...
            ..*
            ...
            3 3
            ***
            **.
            ...
            3 3
            *.*
            ..*
            .**
            3 3
            *..
            .**
            .**
            3 3
            *...
     Output:NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO

    •Input : 100
            3 3
            .*.
            ...
            **.
            3 3
            ***
            ***
            .**
            3 3
            *..
            .**
            .*.
            3 3
            ***
            .**
            **.
            3 3
            ***
            ***
            ..*
            3 3
            ***
            ***
            ..*
            3 3
            .*.
            .*.
            *..
            3 3
            *..
            ..*
            *..
            3 3
            .*.
            ***
            .*.
            3 3
            ..*
            ***
            .*.
            3 3
            .*.
            .*.
            .*.
            3 3
            *.*
            ...
            *..
            3 3
            ..*
            *.*
            ***
            3 3
            .**
            *..
            ***
            3 3
            ..*
            *.*
            .**
            3 3
            **.
            *..
            .*.
            3 3
            ..*
            .**
            .*.
            3 3
            *..
            .*.
            ***
            3 3
            *..
            ...
            *.*
            3 3
            ***
            **.
            ..*
            3 3
            ..*
            .*.
            .*.
            3 3
            .*.
            ..*
            *..
            3 3
            ..*
            .*.
            **.
            3 3
            ..*
            .**
            *..
            3 3
            .*.
            .**
            ..*
            3 3
            *...
     Output:NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            YES
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
            NO
"""