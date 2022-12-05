import customtkinter



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
healthMaxValue = 10
hungerMaxValue = 10
thirstMaxValue = 10

healthCurrentValue = 7
hungerCurrentValue = 1
thirstCurrentValue = 5

root = customtkinter.CTk()
root.title("7 VS WILD")
root.geometry("1000x800")
root.resizable(False, False)


def changemyValue():
    global healthMaxValue
    healthMaxValue += 1
    hungerValueLable["text"] = f"{healthMaxValue}"
    print(healthMaxValue)



# oberer Frame
topBanner = customtkinter.CTkFrame(master=root, height=240)
topBanner.pack(pady=10, padx=10, fill="both")

health = customtkinter.CTkLabel(master=topBanner, text="  Gesundheit ")
health.grid(row=0, column=0)

healthValueLable = customtkinter.CTkLabel(master=topBanner, text=f"  {healthCurrentValue}/{healthMaxValue}")
healthValueLable.grid(row=0, column=1)

hunger = customtkinter.CTkLabel(master=topBanner, text="  Hunger")
hunger.grid(row=1, column=0, sticky=customtkinter.W)

hungerValueLable = customtkinter.CTkLabel(master=topBanner, text=f"  {hungerCurrentValue}/{hungerMaxValue}")
hungerValueLable.grid(row=1, column=1)

thirst = customtkinter.CTkLabel(master=topBanner, text="  Durst")
thirst.grid(row=2, column=0, sticky=customtkinter.W)

thirstValueLable = customtkinter.CTkLabel(master=topBanner, text=f"  {thirstCurrentValue}/{thirstMaxValue}")
thirstValueLable.grid(row=2, column= 1)

#spacerLable = customtkinter.CTkLabel(master=topBanner, text=spacer)
#spacerLable.grid(row=0, column=2)

ClockLable = customtkinter.CTkLabel(master=topBanner, text="Uhrzeit")
ClockLable.grid(row=0, column=3, padx=(750, 0))

clock = customtkinter.CTkLabel(master=topBanner, text="  19:55")
clock.grid(row=0, column=4)



#mittlerer Frame
middleBanner = customtkinter.CTkFrame(master=root, height=240)
middleBanner.pack(pady=10, padx=10, fill="x")

event = customtkinter.CTkLabel(master=middleBanner, text="Randome Text", font=("Arial", 35))
event.pack(pady=(100,100))

#unterer Frame
bottomBanner = customtkinter.CTkFrame(master=root, height=240)
bottomBanner.pack(pady=10, padx=10, fill="x")

buttonUpperLeft = customtkinter.CTkButton(master=bottomBanner, text="Button1", width=300, height=70, command=changemyValue)
buttonUpperLeft.grid(row=0, column=0, padx=(10, 180), pady=(30, 30))

buttonUpperRight = customtkinter.CTkButton(master=bottomBanner, text="Button2", width=300, height=70)
buttonUpperRight.grid(row=0, column=1, padx=(180, 10), pady=(30, 30))

buttonBottomLeft = customtkinter.CTkButton(master=bottomBanner, text="Button3", width=300, height=70)
buttonBottomLeft.grid(row=1, column=0, padx=(10, 180), pady=(30, 30))

buttonBottomRight = customtkinter.CTkButton(master=bottomBanner, text="Button4", width=300, height=70)
buttonBottomRight.grid(row=1, column=1, padx=(180, 10), pady=(30, 30))

root.mainloop()
