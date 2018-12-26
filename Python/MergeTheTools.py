def merge_the_tools(string, k):
    n = len(string)
    increment = k
    unique = []
    for i in range(0, n, increment):
        subsegment = string[i:i + increment]
        for j in range(len(subsegment)):
                aux = sorted(set(subsegment), key=subsegment.index)
                solution = ''.join(aux)
        print(solution)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
