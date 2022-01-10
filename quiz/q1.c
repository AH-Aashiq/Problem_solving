#include<stdio.h>
int main()
{
    int rad,side_length;
    float v_sphere,v_cube;

    printf("Enter Radius:");
    scanf("%d",&rad);
    v_sphere = (4/3.0)*3.1416*rad*rad*rad;
    printf("Volume of Sphere is = %.2f\n",v_sphere);

    printf("Enter side length of cube: ");
    scanf("%d",&side_length);

    v_cube = side_length*side_length*side_length;
    printf("Volume of cube is = %.2f\n",v_cube);

    if (v_sphere > v_cube){
        printf("Sphere container can store more water\n");
    }
    else{
        printf("Cube container can store more water");
    }
    return 0;

}
