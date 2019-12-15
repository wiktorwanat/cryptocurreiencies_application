import tkinter as tk
import Crypto
height=700
width=600

def calculate_crypto_for_dolar(value_in):
    dire=r'C:\Users\WIKUS\Desktop\CRYPTO_VALUES'
    frames=[TETHER_out_frame,BITCOIN_CASH_out_frame,RIPPLE_out_frame,ETHERIUM_out_frame,bitcoin_out_frame]
    values_of_crypto=[Crypto.find_high_daily_value(dire+'\\'+'VALUE_'+'usdt.txt'),Crypto.find_high_daily_value(dire+'\\'+'VALUE_'+'bcc.txt'),Crypto.find_high_daily_value(dire+'\\'+'VALUE_'+'xrp.txt'),Crypto.find_high_daily_value(dire+'\\'+'VALUE_'+'eth.txt'),Crypto.find_high_daily_value(dire+'\\'+'VALUE_'+'btc.txt')]
    i=0
    for frame in frames:

        wynik=Crypto.calculate_value(values_of_crypto[i],value_in)
        print(wynik)
        frame['text']=wynik
        i+=1

def write_crypto_values():
    label_upper_frame['text']=Crypto.writtin()


root=tk.Tk()

#rozmiar okna
canvas=tk.Canvas(root,height=height,width=width)
canvas.pack()
#tlo okna
back_image=tk.PhotoImage(file=r'C:\Users\WIKUS\PycharmProjects\crypto_values_monitor\bitcoin_wallet.png')
back_label=tk.Label(root,image=back_image)
back_label.place(relwidth=1,relheight=1)

#gorny nagloweczek

Main_frame=tk.Frame(root,bd=5,bg='black')
Main_frame.place(relwidth=0.5,relheight=0.05,relx=0.5,rely=0.05,anchor='n')

Name_label=tk.Label(Main_frame,text='WELCOME IN OUR CALCULATOR APP!',bg='black',fg='white',justify='center')#u gory naglowek
Name_label.place(relx=0.1,rely=0)


upper_frame=tk.Frame(root,bg='#cccccc',bd=10)
upper_frame.place(relwidth=0.7,relheight=0.2,relx=0.5,rely=0.15,anchor='n')

label_upper_frame=tk.Label(upper_frame,bg='black',fg='white')
label_upper_frame.place(relwidth=1,relheight=1)
write_crypto_values()
#wpisanie wartosci w dolarach
frame_for_entry=tk.Frame(root,bd=5,bg='#cccccc')
frame_for_entry.place(relwidth=0.5,relheight=0.05,relx=0.5,rely=0.4,anchor='n')

entry = tk.Entry(frame_for_entry, font=40)
entry.place(relwidth=0.7, relheight=1)

button_calculate=tk.Button(frame_for_entry,text="Calculate",bg='blue',fg='white',command=lambda: calculate_crypto_for_dolar(entry.get()))#dodac jescze command jako co ma sie robic po tym przycisku
button_calculate.place(relx=0.7)

#wyniki po przeliczeniu
Frame_for_bitcoin=tk.Label(root,bg='#cccccc',text='BITCOIN',fg='black',justify='center')
Frame_for_bitcoin.place(relx=0.2,rely=0.5)

bitcoin_out_frame=tk.Label(root,bg='#cccccc',bd=1)
bitcoin_out_frame.place(relwidth=0.5,relheight=0.03,relx=0.6,rely=0.5,anchor='n')
########################################################################
Frame_for_ETHERIUM=tk.Label(root,bg='#cccccc',text='ETHERIUM',fg='black',justify='center')
Frame_for_ETHERIUM.place(relx=0.2,rely=0.58)
ETHERIUM_out_frame=tk.Label(root,bg='#cccccc',bd=1)
ETHERIUM_out_frame.place(relwidth=0.5,relheight=0.03,relx=0.6,rely=0.58,anchor='n')
######################################################
Frame_for_RIPPLE=tk.Label(root,bg='#cccccc',text='RIPPLE',fg='black',justify='center')
Frame_for_RIPPLE.place(relx=0.2,rely=0.66)
RIPPLE_out_frame=tk.Label(root,bg='#cccccc',bd=1)
RIPPLE_out_frame.place(relwidth=0.5,relheight=0.03,relx=0.6,rely=0.66,anchor='n')
######################################################
Frame_for_BITCOIN_CASH=tk.Label(root,bg='#cccccc',text='BITCOIN CASH',fg='black',justify='center')
Frame_for_BITCOIN_CASH.place(relx=0.2,rely=0.74)
BITCOIN_CASH_out_frame=tk.Label(root,bg='#cccccc',bd=1)
BITCOIN_CASH_out_frame.place(relwidth=0.5,relheight=0.03,relx=0.6,rely=0.74,anchor='n')
######################################################
Frame_for_TETHER=tk.Label(root,bg='#cccccc',text='TETHER',fg='black',justify='center')
Frame_for_TETHER.place(relx=0.2,rely=0.82)
TETHER_out_frame=tk.Label(root,bg='#cccccc',bd=1)
TETHER_out_frame.place(relwidth=0.5,relheight=0.03,relx=0.6,rely=0.82,anchor='n')
######################################################


root.mainloop()
