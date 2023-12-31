"""
Program_4_Test_Cases:
Lines of Code : 74
Number of Test Cases : 3
Test Cases include:
    •Input : 4
            3
            0 0 1
            4 3 2
            5
            0 4 8 12 16
            2 6 10 14 18
            4
            0 10 10 10
            10 10 10 10
            2
            0 0
            0 0
     Output:5
            19
            17
            3
    
    •Input : 10000
            2
            0 0
            0 0
            2
            0 1
            0 0
            2
            0 0
            1 0
            2
            0 0
            0 1
            2
            0 2
            0 0
            2
            0 1
            1 0
            2
            0 1
            0 1
            2
            0 0
            2 0
            2
            0 0
            1 1
            2
            0 0
            0 2
            3
            0 0 0
            0 0 0
            2
            0 3
            0 0
            2
            0 2
            1 0
            2
            0 2
            0 1
            2
            0 1
            2 0
            2
            0 1
            1 1
            2
            0 1
            0 2
            2
            0 0
            3 0
            2
            0 0
            2 1
            2
            0 0
            1 2
            2
            0 0
            0 3
            3
            0 1 0
            0 0 0
            3
            0 0 1
            0 0 0
            3
            0 0 0
            1 0 0
            3
            0 0 0
            0 1 0
            3
            0 0 0
            0 0 1
            2
            0 4
            0 0
            2
            0 3
            1 0
            2
            0 3
            0 1
            2
            0 2
            2 0
            2
            0 2
            1 1
            2
            0 2
            0 2
            2
            0 1
            3 0
            2
            0 1
            2 1
            2
            0 1
            1 2
            2
            0 1
            0 3
            2
            0 0
            4 0
            ...
     Output:3
            3
            3
            3
            3
            4
            3
            3
            3
            4
            5
            4
            4
            3
            4
            4
            4
            4
            3
            4
            5
            5
            5
            5
            5
            5
            5
            4
            4
            5
            4
            4
            4
            4
            4
            5
            5
            4
            4
            5
            6
            5
            5
            6
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            6
            5
            5
            5
            4
            4
            5
            5
            4
            5
            5
            4
            4
            5
            6
            6
            5
            4
            5
            6
            7
            7
            5
            5
            6
            5
            5
            5
            6
            5
            5
            6
            6
            6
            6
            5
            5
            5
            6
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            5
            7
            6
            6
            5
            5
            5
            6
            5
            4
            5
            5
            5
            5
            5
            6
            6
            5
            4
            5
            6
            7
            7
            6
            5
            5
            6
            7
            8
            7
            7
            7
            7
            7
            7
            7
            5
            5
            6
            5
            5
            5
            6
            5
            5
            7
            6
            6
            6
            5
            5
            5
            6
            5
            5
            6
            6
            6
            6...

    •Input : 10000
            14
            0 1 4 2 1 7 6 10 4 0 3 7 7 3
            4 2 1 8 0 2 4 2 10 7 9 1 7 9
            2
            0 9
            9 0
            2
            0 3
            10 6
            15
            0 7 2 6 6 9 6 8 3 2 6 10 7 8 2
            5 2 10 7 9 0 9 2 3 3 2 8 7 2 4
            3
            0 5 0
            9 6 0
            2
            0 2
            9 5
            8
            0 1 7 4 3 10 1 1
            5 5 1 6 10 2 1 3
            4
            0 6 3 6
            1 5 1 5
            5
            0 10 8 0 6
            3 5 5 5 8
            6
            0 5 6 5 2 10
            3 10 1 1 6 1
            2
            0 9
            3 1
            4
            0 8 5 8
            0 3 5 1
            5
            0 8 2 6 9
            8 10 10 0 9
            7
            0 3 10 6 5 4 1
            7 8 6 8 2 0 0
            13
            0 7 5 1 1 2 10 3 8 8 5 7 9
            6 3 7 1 4 10 8 8 3 10 0 9 4
            6
            0 0 9 3 4 0
            2 4 1 6 4 5
            8
            0 1 9 6 10...
     Output:31
            12
            11
            34
            10
            10
            20
            11
            13
            17
            10
            11
            17
            20
            31
            14
            22
            12
            14
            11
            11
            4
            6
            11
            22
            5
            6
            12
            15
            23
            24
            12
            14
            16
            13
            12
            11
            24
            21
            13
            15
            16
            9
            10
            18
            7
            13
            10
            11
            22
            12
            12
            56
            10
            29
            12
            6
            11
            12
            11
            11
            9
            20
            16
            12
            12
            11
            20
            24
            10
            17
            10
            10
            17
            13
            32
            11
            6
            11
            22
            12
            12
            8
            23
            10
            16
            17
            21
            12
            12
            21
            11
            13
            15
            10
            21
            14
            13
            39
            9
            21
            15
            11
            4
            9
            12
            35
            28
            22
            15
            16
            29
            11
            11
            32
            5
            9
            13
            10
            18
            9
            20
            16
            19
            11
            9
            12
            7
            11
            15
            11
            13
            2...
"""