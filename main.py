from graphics import *
import csv

outerloop=False
while True:
    data_list = []   # data_list An empty list to load and hold data from csv file

    def load_csv(CSV_chosen):
        """
        This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
        YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
        """
        try:
            with open(CSV_chosen, 'r') as file:
                csvreader = csv.reader(file)
                header = next(csvreader)
                for row in csvreader:
                    data_list.append(row)
            return True
        except Exception as e:
            print(f"The following error has occured:{e}")
            return False


    #************************************************************************************************************

    def print_and_save(string1): #For printing and writing to the file at the same time
        print(string1)
        with open("results.txt","a") as f:
            f.write(string1+"\n")

    #Harcoded strings for airport/airline code and name
    airport_code=['LHR','MAD','CDG','IST','AMS','LIS','FRA','FCO','MUC','BCN']
    full_airport_name={
        airport_code[0]:"London Heathrow",
        airport_code[1]:"Madrid Adolfo Suárez-Barajas",
        airport_code[2]:"Charles De Gaulle International",
        airport_code[3]:"Istanbul Airport International",
        airport_code[4]:"Amsterdam Schiphol",
        airport_code[5]:"Lisbon Portela",
        airport_code[6]:"Frankfurt Main",
        airport_code[7]:"Rome Fiumicinos",
        airport_code[8]:"Munich International",
        airport_code[9]:"Barcelona International",
    }
    airline_code=['BA','AF','AY','KL','SK','TP','TK','W6','U2','FR','A3','SN','EK','QR','IB','LH']
    full_airline_name={
        airline_code[0]:'British Airways',
    airline_code[1]:'Air France',
    airline_code[2]:'Finnair',
    airline_code[3]:'KLM',
    airline_code[4]:'Scandinavian Airlines',
    airline_code[5]:'TAP Air Portugal',
    airline_code[6]:'Turkish Airlines',
    airline_code[7]:'Wizz Air',
    airline_code[8]:'easyJet',
    airline_code[9]:'Ryanair',
    airline_code[10]:'Aegean Airlines',
    airline_code[11]:'Brussels Airlines',
    airline_code[12]:'Emirates',
    airline_code[13]:'Qatar Airways',
    airline_code[14]:'Iberia',
    airline_code[15]:'Lufthansa'}

    #Validating input and returning city code with year
    def input_validation():
        """
        This function asks for city code and year until and unless the input is valid"
        """
        while True:
            city_code:str=input("Please enter the three-letter code for the departure city required in the format XXX:")
            if len(city_code)==3:
                if city_code.upper() in airport_code:
                    break
                else:
                    print("Unavailable city code - please enter a valid city code:(XXX)")
            else:
                print("Wrong code length - please enter a three-letter city code:(XXX)")

        while True:
            year=input("Please enter the year required in the format YYYY:")#can't be int,as it converts input to string directly
            if year.isdecimal():#Expects string
                if len(year)==4:#Expects string
                    if int(year)>=2000 and int(year)<=2025:#Expects int
                        break
                    else:
                        print("Out of range - please enter a value from 2000 to 2025:(YYYY)")
                else:
                    print("Wrong length - please enter a four-digit year value:(YYYY)")
            else:
                print("Wrong data type - please enter a four-digit year value:(YYYY)")

        return (city_code.upper(),year)

    #Fetches airport code and year for a csv file
    code_and_year=""
    def csv_filename_compute():
        global code_and_year
        code_and_year=input_validation()
        csv_filename=f'{code_and_year[0]}{code_and_year[1]}.csv'
        return(csv_filename)
    selected_data_file=csv_filename_compute()

    #Checks if the input csv is valid or not
    successful_load=load_csv(selected_data_file)
    if not successful_load:
        break

    def print_file_airport_year():
        print_and_save("******************************")
        print_and_save(f"File {selected_data_file} selected - Planes departing {full_airport_name[code_and_year[0]]} {code_and_year[1]}")
        print_and_save("******************************")
    print_file_airport_year()


    #Prints all outcomes in a single function 
    def outcomes():
        """
        This function calculates all the necessary outcomes by accessing the required csv file,prints it in the terminal and saves it in a txt file"
        """
        total_flights=len(data_list)#1

        terminal2_total_flights=0 #2
        for num in range(len(data_list)):#2
            if data_list[num][8]=='2':
                terminal2_total_flights+=1
        
        flights_600miles=0#3
        for num in range(len(data_list)):#3
            if int(data_list[num][5])<600:
                flights_600miles+=1

        air_france_total_flights=0 #4
        for num in range(len(data_list)):#4
            if (data_list[num][1][:2])=='AF':
                air_france_total_flights+=1

        temp_15_total_flights=0 #5
        for num in range(len(data_list)):#5
            if int(data_list[num][10][:2])<15:
                temp_15_total_flights+=1
        
        british_airways_total_flights=0 #6 
        for num in range(len(data_list)):#6
            if (data_list[num][1][:2])=='BA':
                british_airways_total_flights+=1
        british_airways_avg_flights=(british_airways_total_flights/12)

        british_airways_percent_total_departure=(british_airways_total_flights/total_flights)*100 #7
        
        air_france_total_delayed_departure=0 #8 
        for num in range(len(data_list)):#8
            if (data_list[num][1][:2])=='AF':
                if (data_list[num][2]!=data_list[num][3]):
                    air_france_total_delayed_departure+=1
        air_france_percentage_delayed_departure=(air_france_total_delayed_departure/air_france_total_flights)*100

        valid_hours=["00","01","02","03","04","05","06","07","08","09","10","11"]#9
        raining_hours=set()
        for num in range(len(data_list)):
            if "rain" in data_list[num][10] and data_list[num][2][:2] in valid_hours:#Checks rain in weather conditions and given hour in valid hours from scheduled departures
                raining_hours.add(data_list[num][2][:2])
        total_hours_rain=len(raining_hours)#Gives the length of all the hours that rained

        dict_destinations={}#10
        for x in range(len(data_list)): #To find the lowest count of least appeared destination
            dest_short_form=data_list[x][4]
            if dest_short_form in dict_destinations:
                dict_destinations[dest_short_form]+=1
            else:
                dict_destinations[dest_short_form]=1
        least_value=min(dict_destinations.values())
        least_destination=[] #To get the name/append if two or more least destination
        for x in dict_destinations:
            if dict_destinations[x]==least_value:
                least_destination.append(x)
        least_destination_full_names=[]
        for x in range(len(least_destination)):
            least_destination_full_names.append(full_airport_name[least_destination[x]])

    #Prints the required information in the terminal and saves them in a text file 
        print_and_save(f"The total number of flights from this airport was {total_flights}")
        print_and_save(f"The total number of flights departing Terminal Two was {terminal2_total_flights}")
        print_and_save(f"The total number of departures on flights under 600 miles was {flights_600miles}")
        print_and_save(f"There were {air_france_total_flights} Air France flights from this airport")
        print_and_save(f"There were {temp_15_total_flights} flights departing in temperatures below 15 degrees")
        print_and_save(f"There was an average of {british_airways_avg_flights:.2f} British Airways flights per hour from this airport")
        print_and_save(f"British Airways planes made up {british_airways_percent_total_departure:.2f}% of all departures")
        print_and_save(f"{air_france_percentage_delayed_departure:.2f}% of Air France departures were delayed")
        print_and_save(f"There were {total_hours_rain} hours in which rain fell")
        print_and_save(f"The least common destinations are {least_destination_full_names}")

    outcomes()

    def histogram():
        """
        This function checks an appropriate airline code,fetches necessary data and plots a histogram for the given data
        """
        dict_hours_departure={"00":0,"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0}
        while True:
            histogram_airline_code=input("Enter a two-character Airline code to plot a histogram in the format XX:")
            if histogram_airline_code.upper() in airline_code:
                break
            else:
                print("Unavailable Airline code please try again:(XX)")
        title=f" Departures by hour for {full_airline_name[histogram_airline_code.upper()]} from {full_airport_name[code_and_year[0]]} {code_and_year[1]}"

        #Fetch data
        hours=["00","01","02","03","04","05","06","07","08","09","10","11"]
        for num in range(len(data_list)):
            if data_list[num][1][:2]==histogram_airline_code.upper():
                for x in hours:
                    if data_list[num][2][:2]==x:
                        dict_hours_departure[x]+=1
                        break

        win=GraphWin("Histogram",800,600)
        win.setBackground("beige")

        data=[]
        labels=[]
        for key,value in dict_hours_departure.items():
            labels.append(key)
            data.append(value)

        #Defining constants for histogram
        x_origin=100
        y_start=70
        bar_height=30
        gap=0
        max_value=max(data)
        max_bar_length=400  #How much horizontal space bars can take
        scale=max_bar_length/max_value

        lastbar_bottom=y_start+len(data)*(bar_height+gap)-gap

        #Drawing axes
        Line(Point(x_origin,70), Point(x_origin,lastbar_bottom)).draw(win)  #Y-axis

        #Drawing bars horizontally
        for i in range(len(data)):
            width=data[i]*scale
            x1=x_origin
            x2=x_origin + width
            y1=y_start + i * (bar_height + gap)
            y2=y1+bar_height


            if data[i]!=0:
                bar=Rectangle(Point(x1,y1),Point(x2,y2))
                bar.setFill("#FCBE6A")
                bar.setOutline("black")
                bar.draw(win)
                Text(Point(x2 + 20,(y1+y2)/2),str(data[i])).draw(win) # Value at the end of bar

            # Label to the left of bar
            hours_label=Text(Point(x_origin-20,(y1+y2)/2),labels[i])
            hours_label.setSize(11)#Adjusting font size
            hours_label.draw(win)

        mid_point_yaxis=(y_start+lastbar_bottom)/2 #Alignment for the left label
        Text(Point(x_origin-70,(mid_point_yaxis)),"Hours").draw(win)
        Text(Point(x_origin-70,(mid_point_yaxis+30)),"00:00").draw(win)
        Text(Point(x_origin-70,(mid_point_yaxis+50)),"to").draw(win)
        Text(Point(x_origin-70,(mid_point_yaxis+70)),"12:00").draw(win)

        Text(Point(300,20),title).draw(win)
        win.getMouse()
        win.close()

    histogram()
    #Loops the program by asking inputs and plotting histogram if user allows
    while True:
        new_analysis=input("Do you want to select a new data file? Y/N:")
        if new_analysis.upper()=='N':
            print("End of program")
            outerloop=True
            break
        elif new_analysis.upper()=='Y':
            break
        else:
            print("Wrong input. Please select Y/N:")
    if outerloop==True:
        break