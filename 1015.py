#Distance Between Two Points
import  math

x1,y1=list(map(float,input().split()))                              
x2,y2=list(map(float,input().split()))
distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

print(f'{distance:0.4f}')

