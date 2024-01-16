one = 1
print("Chương trình tìm nghiệm của phương trình bậc 2")
#Lặp lại chương trình
while True:
    #Câu lệnh try kiểm tra các hệ số a,b,c đầu vào
    try:
        a = float(input("\nNhập hệ số a: "))
        so_nguyen_a = int(a)
        #Kiểm tra giá trị của hệ số a, và yêu cầu nhập đến khi a có một giá trị hợp lí
        while so_nguyen_a+one==one: #Nếu a là 0 thì 0+1=1 => True và yêu cầu nhập lại a
            #In ra thông báo khi a không có giá trị hợp lệ
            print("a không được bằng 0, vui lòng nhập lại")
            a = float(input("\nNhập hệ số a: "))
            so_nguyen_a = int(a)
            if so_nguyen_a!=0: #Kiểm tra hệ số a vừa mới nhập, nếu a!=0 thì a*1=a
                break #Hủy nhập a nếu a đã khác 0
            else: #Nếu a tiếp tục là 0, tiếp tục hỏi a
                continue
        b = float(input("Nhập hệ số b: ")) #Nhập hệ số b
        c = float(input("Nhập hệ số c: ")) #Nhập hệ số c
    #Lệnh except thông báo lỗi nếu dự liệu đầu vào sai
    except:
        print("Dữ liệu sai, vui lòng nhập một số! ")

    #Block else sẽ được thực hiện nếu không có lỗi nào từ khâu nhập các hệ số a, b, c
    else:
        #In ra phương trình bậc 2 dựa trên các hệ số a, b, c
        print(f"\nPhương trình bậc 2 của bạn: ({int(a)}x^2)+({int(b)}x)+({int(c)}) ")
        #Tính delta
        delta = b ** 2 - 4 * a * c #Công thức tính delta
        print(f"Giá trị của delta là: {delta} ") #In ra giá trị của delta
        if delta > 0: #Trường hợp delta > 0
            print("Vì delta > 0 nên phương trình có 2 nghiệm phân biệt x1, x2: ")
            x1 = (-b + (delta ** (1 / 2))) / (2 * a) #Công thức tính x1
            print("x1:", x1) #In ra giá trị của x1
            x2 = (-b - (delta ** (1 / 2))) / (2 * a) #Công thức tính x2
            print("x2:", x2) #In ra giá trị của x2
        elif delta < 0: #Trường hợp delta < 0
            print("Vì delta < 0 nên phương trình vô nghiệm! ")
        else: #Trường hợp delta = 0
            x = -b / (2 * a) #Công thức tính x khi delta = 0
            print("Giá trị của x khi delta bằng 0: ", x)


            #chinh sua