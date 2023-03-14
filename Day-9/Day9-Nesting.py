
# {
    # Key1: [list],
    # Key2: {Dictionary} 
# }
#Nesting List in a dictionary
travel_log1 = {
    "TN" : ["Madras","Coimbatore", "Trichy"],
    "KA" : ["Bangalore","Mangalore","Mysore"],
    "AP" : ["Hyderabad","Secundrabad","Amaravathi"]
}

for tr_log in travel_log1:
    print (tr_log)
    print (travel_log1[tr_log])


#Nesting Dictionary in a dictionary
travel_log2 = {
    "TN" : {"cities_visited":["Madras","Coimbatore", "Trichy"], "total_visits": 12},
    "KA" : {"cities_visited":["Bangalore","Mangalore","Mysore"], "total_visits": 13},
    "AP" : {"cities_visited":["Hyderabad","Secundrabad","Amaravathi"], "total_visits": 14}
}

#Nesting Dictionary in a List
travel_log3 = [                                                  #Beginning of a list
    {                                                            #Beginning of a dictionary
    "state": "TN",
    "cities_visited":["Madras","Coimbatore", "Trichy"], 
    "total_visits": 12
    },
   {
    "state": "KA",
    "cities_visited":["Bangalore","Mangalore","Mysore"],
    "total_visits": 13
    },
    {
    "state" :"AP",
    "cities_visited":["Hyderabad","Secundrabad","Amaravathi"], 
    "total_visits": 14
    }
]

