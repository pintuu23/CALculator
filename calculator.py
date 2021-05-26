
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2




operation_dict={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
# function= operation_dict["+"]
# y=function(n_1,n_2)
#
# print(y)
def cal():
    num1=int(input("What is the first number? :" ))

    for symbol in operation_dict:
        print(symbol)

    should_continue=True
    while should_continue:
        operation = input("What is the operation you want to perform? :")
        num2 = int(input("What is the next number? : "))

        function = operation_dict[operation]
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        if input("do you want to continue the calculation ? type 'y' for yes or 'n' for exit ")=="y":
            num1=answer
        else:
            should_continue= False
            cal()
cal()