#include<iostream>

using namespace std;

int fib(int n){

	int a=0;
	int b=1;
	int x=0;
	
	x=x+fib(n-1)+fib(n-2);

	cout<<x<<" ";
	// if(n>1){
	// 	return fib(n-2)+fib(n-1);
	// }
	// else{
	// 	return 1;
	// }
	return 0;
}

int main(){
	int n;
	cin>>n;
	cout<<"Recursive ";
	fib(n);
	cout<<endl;
	cout<<"Non Recursive ";
	int y=0,t1=0,t2=1;
	for(int i=1;i<=n;i++){
		y=t1+t2;
		t1=t2;
		t2=y;
		cout<<y;
	}
	
	return 0;
}