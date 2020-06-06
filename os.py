def vies_dir(path='.'):
    names=os.listdir(path)
    names.sort()
    for name in names:
        print(name,end=' ')
    print()

