from tkinter import *
from tkinter import messagebox
 
def display_mass_nagr():
    M_cn = N.get()*m.get()
    M = M_cn * 1.1/(1 - m_con.get() - m_t.get() - m_s.get() - m_su.get())
    messagebox.showinfo("Массы", "Масса целевой нагрузки: " + str(M_cn) + " кг\n" 
                                "Полная масса: " + str(M) + " кг")



root = Tk()
root.title("Графический интерфейс")
root.geometry("500x300")


N = IntVar()
m = DoubleVar()
m_con = DoubleVar()
m_t = DoubleVar()
m_s = DoubleVar()
m_su = DoubleVar()
 
N_label = Label(text="Количество людей на борту:")
m_label = Label(text="Масса человека с багажом:")
m_con_label = Label(text="Масса m_con:")
m_t_label = Label(text="Масса m_t:")
m_s_label = Label(text="Масса m_s:")
m_su_label = Label(text="Масса силовой установки:")


 
N_label.grid(row=0, column=0, sticky="w")
m_label.grid(row=1, column=0, sticky="w")
m_con_label.grid(row=2, column=0, sticky="w")
m_t_label.grid(row=3, column=0, sticky="w")
m_s_label.grid(row=4, column=0, sticky="w")
m_su_label.grid(row=5, column=0, sticky="w")
 
N_entry = Entry(textvariable=N)
m_entry = Entry(textvariable=m)
m_con_entry = Entry(textvariable=m_con)
m_t_entry = Entry(textvariable=m_t)
m_s_entry = Entry(textvariable=m_s)
m_su_entry = Entry(textvariable=m_su)

 
N_entry.grid(row=0,column=1, padx=5, pady=5)
m_entry.grid(row=1,column=1, padx=5, pady=5)
m_con_entry.grid(row=2,column=1, padx=5, pady=5)
m_t_entry.grid(row=3,column=1, padx=5, pady=5)
m_s_entry.grid(row=4,column=1, padx=5, pady=5)
m_su_entry.grid(row=5,column=1, padx=5, pady=5)
 
 
message_button = Button(text="Рассчитать массы нагрузки", command=display_mass_nagr)
message_button.grid(row=6,column=1, padx=5, pady=5, sticky="e")










root.mainloop()



# N = 10
# m = 77 + 15.0
# m_con = 0.28
# m_t = 0.25
# m_s = 0.1
# m_su = 0.18

# def Mas_0(N, m, m_con, m_t, m_s, m_su):
#     M_cn = N * m
#     M = M_cn * 1.1/(1 - m_con - m_t - m_s - m_su)
#     return (M_cn, M)

# M = Mas_0(N, m, m_con, m_t, m_s, m_su)
# print(M)
