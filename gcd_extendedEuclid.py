def egcd(a,b):
    #initialise
    rn=b
    rnmin=a
    rnplus=a%b
    q1=int(rnmin/rn)
    uN=0
    vN=1
    uNplus=1-(q1*uN)
    uNmin=1
    vNplus=0-(q1*vN)
    vNmin=0
    #print(rnmin,rn,rnplus,uNmin,uN,uNplus,vNmin,vN,vNplus) # checking initialisation for n=1
    while(rnplus != 0):
        rnmin=rn
        #print('R N-1',rnmin)
        rn=rnplus
        #print('R N',rn)
        rnplus=rnmin%rn
        #print('R N+1',rnplus)
        q1=int(rnmin/rn)
        uNmin=uN
        uN=uNplus
        uNplus=uNmin-(q1*uN)
        vNmin=vN
        vN=vNplus
        vNplus=vNmin-(q1*vN)

    return rn,uN,vN
        
print("Larger Number: ")
a=int(input())
print("Smaller Number: ")
b=int(input())
gcd,u,v=egcd(a,b)
print("GCD is: ",gcd)
print("u is: ",u)
print("v is: ",v)

