

# a="vijay"
# print("the message is ",a)

# a="vijay"
# print("the message is ",a)
# a="prasanth"
# print("the changed message is ",a)


# menu_card=['panner','dal','rice']


# menu_card.append('channa')
# print('adding element at the last : ',menu_card)

# menu_card.extend(['briyani','bbq'])
# print(menu_card)

# menu_card.insert(1,'prawn')
# print(menu_card)

# menu_card.remove('dal')
# print(menu_card)

# menu_card.pop(2)
# print(menu_card)

# index_method=menu_card.index('briyani')
# print(index_method)

# index_method=menu_card.index('bbq')
# print(index_method)

# menu_card.sort()
# print(menu_card)


# print('slicing',menu_card[1:3])

# for name in menu_card:
#     print(f'{name} menu ')

# for name in menu_card:
#     print(f'{name.upper()} menu')



# 1) Create a menu_card list
# veg_starter = ['paneer 65','chilly paneer','veg crispy']
# 1) Display menu card
# 2)Add Starter in the menu card
# 3)Update Starter in the menu card
# 4)Remove Starter in the menu card
 
# Example:
# Add : Which starter you want to add in menu?
# paneer roll
# ['Paneer 65','Chilly paneer','Veg crispy','Paneer roll']
# Added Successfully


# def main():

#     size=int(input('enter how many dishes you want to add in menu card : '))
#     data_input=[]
#     print('enter the dishes: ')
#     for i in range(size):
#         dishes=input()
#         data_input.append(dishes)
#     print('the dishes are : ',data_input)
#     data_input=add(data_input)
#     print('dish added successfully')
#     print('the dishes are : ',data_input)
#     data_input=update(data_input)
#     print('the dishes are : ',data_input)
#     data_input=remove(data_input)
#     print('the dishes are : ',data_input)

# print()

# def add(data_input):
    
#     print('Which starter you want to add in menu? ')
#     add_dish=input()
#     data_input.append(add_dish)
#     return data_input

# print()

# def update(data_input):

#     print('where you want to update : ')
#     update_dish=input()
#     if update_dish in data_input:
#         new_value = input('enter new dish : ')
#         index=data_input.index(update_dish)
#         data_input[index] = new_value
#         print(f'Updated {update_dish} to {new_value}.')
#     else:
#         print(f'Key {update_dish} not found in the data.')
#     return data_input
# print()

# def remove(data_input):

#     print('which dish you want to remove : ')
#     remove_dish=input()
#     data_input.remove(remove_dish)
#     return data_input

# if __name__ == "__main__":
#     main()




#    2. 


def main():

    size=int(input('enter the size: '))
    result_1=[]

    for i in range(size):
        value=int(input())

        result_1.append(value)
    print(result_1)
    addition(result_1)
    max(result_1)

    
def addition(result_1):

    sum=0

    for index in result_1:
        sum+=index
    print(sum)

def max(result_1):

    maximum=0

    for maxi in result_1:

        if(maximum<maxi):
            maximum=maxi
    print(maximum)










if __name__ == "__main__":
    main()


        



     

    



