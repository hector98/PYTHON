if __name__ == '__main__':

    ins="Insuficiente: "
    su="suficiente: "
    bi="Bien: "
    ex="Excelente: "

    for cont in range(1, 21):
        print("Escribe la calificacion", cont)
        cal=float(input())
        if cal <= 5.9:
            ins += str(cal)+'\n '
        if cal >= 6 and cal <= 7.9:
            su += str(cal)+'\n'
        if cal >= 8 and cal <= 9.9:
            bi += str(cal)+'\n'
        if cal == 10:
            ex += str(cal)+'\n'

    print(ins+'\n'+ su +'\n'+ bi +'\n'+ ex)
