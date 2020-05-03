from os import system
def img():
      if x==1:
        y=input("enter the name of img")
        z=input("u want version y/n if n it will take latest").lower()
        if z=='y':
            a=input("enter the version eg 0.2")
            system(f"docker pull {y}:{a}")
        else:
            system(f"docker pull {y}")
def seeimg():
    system(f"docker image ls")
def seecon():
    print("all the containers")
    system("docker ps -a")
    print("all the running container")
    system("docker ps")
def attach():
    name=input("enter the name of docker")
    system(f"docker restart {name}")
    z=input("u want to attach to docker y/n")
    if z=='y':
        system(f"docker attach {name}")
def rmimg():
    seeimg()
    name=input()
    system(f"docker image rm -f {name}")
def rmcon():
    seecon()
    name=input()
    system(f"docker container rm -f {name}")
("\t\t\tWelcome to docker automation")
system("systemctl start docker")
while True:
    print("""\t\t\tpress 1 to pull img
             \t\t\tpress 2 to run docker
             \t\t\tpress 3 to make your own img
             \t\t\tpress 4 to make your own network
             \t\t\tpress 5 to make your own permanent storage
             \t\t\tpress 6 to see img
             \t\t\tpress 7 to see container
             \t\t\tpress 8 to remove container
             \t\t\tpress 9 to remove img
             \t\t\tpress 10 to exit
             \t\t\tpress 11 to attach
             \t\t\tpress 12 to remove network
             \t\t\tpress 13 to remove storage""")
    x=int(input())
    if x==1:
        img()
    elif x==2:
        k=""
        print("the img u have")
        p=system("docker image ls")
        print(p)
        z=input("enter image name:version")
        p="null"
        p=system(f"docker image ls|grep {z}")
        if p!=z:
            img()
        i=input("u want to run on back  y/n ").lower()
        if i=='y':
            k=k+" -d "
        i=input("u want to add name y/n ").lower()
        if i=='y':
            name=input("enter the new name")
            k=k+" --name "+name
        i=input("u want to add network y/n").lower()
        if i=='y':
            name=input("enter the name of network")
            k=k+" --network "+name
        i=input("u want to add volume y/n").lower()
        if i=='y':
            name=input("enter the name of volume or directory")
            name1=input("enter the directory where u want to copy")
            k=k+" --v "+name+":"+" "+name1
        k=k+" "+z
        system(f"docker run -it{k}")
    elif x==3:
        name=input("enter name or id of the container")
        name1=input("name of the img")
        system(f"docker commit {name} {name1}")
    elif x==4:
        name=input("enter a new network name")
        name1=input("name of driver host null bridge")
        if name1=="host" or name1=="null":
            print("plz remove first there must be one ")
        else:
            system(f"docker network create --driver {name1} name")
    elif x==5:
        name=input("enter a new voltage name")
        system(f"docker volume create {name}")
    elif x==6:
        seeimg()
    elif x==7:
        seecon()
    elif x==8:
        rmcon()
    elif x==9:
        rmimg()   
    elif x==10:
        break
        system.exit(0)
    elif x==11:
        attach()
    elif x==12:
        name=input("enter the network name")
        system(f"docker network rm -f {name}")
    elif x==13:
        name=input("enter the volume name")
        system(f"docker volume rm -f {name}")
