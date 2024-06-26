import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def lucky_number():
    matrix = np.array([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]])
    print(np.min(matrix[1]))
    print(np.shape(matrix)[0])
    min_in_rows=[]

    for i in matrix:
        min_in_rows.append(np.min(i))
    max_in_col = np.max(min_in_rows)
    print(max_in_col)

def histogram():
    matrix = np.random.randint(0,100,(10000))
    print(matrix.shape)
    plt.hist(matrix,bins=10,edgecolor="white")
    plt.xlabel('randomInts')
    plt.ylabel('count')
    plt.title("Counts of random Integers")
    plt.show()
def np_basics():
    B = np.arange(0,25)
    print(B)
    B= B.reshape((5,5))
    print(B)
    x=B[1]
    z=[]
    for i in B:
        z.append(i[-1])
    print(x,z)
    t = B.transpose()
    print(t)




def input_matrix(n):
    matrix = []
    for i in range(n):
        row = input(f"Enter the coefficients for equation {i+1}, separated by spaces (constant term last): ").split()
        matrix.append([float(coef) for coef in row])
    return matrix

def linear_equation():
    try:
        # Prompt the user for the number of variables
        n = int(input("Enter the number of variables in the system: "))

        # Input the coefficient matrix and the constant terms
        print("For each equation, enter the coefficients followed by the constant term.")
        augmented_matrix = input_matrix(n)

        # Separate the coefficient matrix (A) and the constants (b)
        A = np.array([row[:-1] for row in augmented_matrix])
        b = np.array([row[-1] for row in augmented_matrix])

        # Solve the system of equations
        solution = np.linalg.solve(A, b)

        # Print the solution
        for i in range(n):
            print(f"Variable {i+1} = {solution[i]}")

    except ValueError as e:
        print("Invalid input. Please enter numerical values only.")
    except np.linalg.LinAlgError as e:
        print("The system of equations cannot be solved:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


def np_extract():
    K = np.random.randint(100, 500, 7 * 7).reshape(7, 7)
    K[2, 6] = 250
    K[3, 3] = 250
    print(K)
    x=K[K>=250]
    print(x)
    y = np.where(K==250)
    print(y)
def trignometry():
    # Step 1: Plot the functions
    # a. Create an array x of 10,000 evenly spaced numbers between 0 and 2π.
    x = np.linspace(0, 2 * np.pi, 10000)

    # b. Create the first function y1 = 10 sin(3x).
    y1 = 10 * np.sin(3 * x)

    # c. Create the second function y2 = 5 cos(2x).
    y2 = 5 * np.cos(2 * x)

    # d. Plot both functions on the same graph with appropriate labels, title, and grid.
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='y1 = 10 sin(3x)')
    plt.plot(x, y2, label='y2 = 5 cos(2x)')
    plt.title('Plot of y1 = 10 sin(3x) and y2 = 5 cos(2x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Step 2: Find intersection points
    # a. Set an epsilon value of 0.01 to determine the precision of intersection points.
    epsilon = 0.01

    # b. Loop through the arrays and find the points where the absolute difference between y1 and y2 is less than epsilon.
    intersection_points = []

    for i in range(len(x)):
        if abs(y1[i] - y2[i]) < epsilon:
            intersection_points.append((x[i], y1[i]))

    # c. Print the intersection points.
    for point in intersection_points:
        print(f"Intersection at x = {point[0]:.4f}, y = {point[1]:.4f}")

    # Step 3: Plot the functions again and highlight the intersection points
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='y1 = 10 sin(3x)')
    plt.plot(x, y2, label='y2 = 5 cos(2x)')
    plt.scatter([p[0] for p in intersection_points], [p[1] for p in intersection_points], color='red', label='Intersections')
    plt.title('Plot of y1 = 10 sin(3x) and y2 = 5 cos(2x) with Intersections')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def movies_operations():
    movies_sheet1=pd.read_excel('./dataset/movies.xlsx',sheet_name="1900s")
    movies_sheet2=pd.read_excel('./dataset/movies.xlsx',sheet_name="2000s")
    movies_sheet3=pd.read_excel('./dataset/movies.xlsx',sheet_name="2010s")
    movies = pd.concat([movies_sheet1, movies_sheet2,
                        movies_sheet3], ignore_index=True)
    print(movies.head())
    print(movies.shape)
    print(movies.tail())
    print(movies.info())
    print(movies.describe())
    sorted_movies_by_grossEarnings = movies.sort_values(by="Gross Earnings",ascending=False)
    print(sorted_movies_by_grossEarnings[["Title","Year","Gross Earnings"]].head())
    boolean_mask = (movies['Year']<1925) & (movies['IMDB Score']>7)
    print(movies[boolean_mask][["Title","Year","IMDB Score"]].head())

    plt.hist(movies['Year'],bins=30,edgecolor="white")
    plt.xlabel('Years')
    plt.ylabel("Count")
    plt.title("Movies per years")
    plt.show()
    index_of_max_IMDB_score=movies['IMDB Score'].idxmax()
    print(movies.iloc[index_of_max_IMDB_score])
    print(movies['Duration'].mean())
    duration_less_than_60_minutes = movies[(movies['Duration']<= 60)][["Duration"]]
    duration_between_60_and_120_minutes= movies[(movies['Duration']> 60) & (movies['Duration'] <=120)][["Duration"]]
    duration_between_120_and_180_minutes= movies[(movies['Duration']> 120) & (movies['Duration']<=180)][["Duration"]]
    duration_above_180_minutes=movies[movies['Duration']>180][["Duration"]]
    # print(duration_less_than_60_minutes,duration_between_60_and_120_minutes.shape[0],duration_between_120_and_180_minutes.shape[0],duration_above_180_minutes.shape[0])
    values=[duration_less_than_60_minutes.shape[0],duration_between_60_and_120_minutes.shape[0],duration_between_120_and_180_minutes.shape[0],duration_above_180_minutes.shape[0]]
    categories=["below 60","61-120","121-180","above 180"]
    plt2 = plt
    plt2.pie(values,labels=categories,autopct="%1.1f%%")
    plt2.title("Categories of duration")
    plt2.show()



while True:
    user_input = str(input("Enter exercise number (1-) or 'q' to exit: "))

    match user_input:
        case "1":
            lucky_number()
        case "2":
            histogram()

        case "3":
            np_basics()
        case "4":
            linear_equation()
        case "5":
            np_extract()
        case "6":
            trignometry()
        case "7":
            movies_operations()
        case "q":
            exit()




