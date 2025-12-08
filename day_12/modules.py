# Day 12: 30 Days of python programming
# Exercises : Level 1
import random
import string
def random_user_id():
        character= string.ascii_letters+string.digits
        picked_char=random.choices(character,k=5)
        joined=''.join(picked_char)
        return joined
print(random_user_id())

def user_id_gen_by_user():
        character= string.ascii_letters+string.digits
        k=int(input('Please input the number of characters'))
        n=int(input('Please input the amount of IDs needed'))
        
        i=0
        while i<n:
            picked_char=random.choices(character,k=k)        
            joined=",".join(picked_char)
            print(joined)
            i+=1
user_id_gen_by_user()
def rgb_color_gen():
       rgb_list=[]
       i=0
       while i<3:
            picked_color=random.randint(0,255)
            rgb_list.append(str(picked_color))
            i+=1
       rgb=",".join(rgb_list)
       print(f"rgb ({rgb})")
rgb_color_gen()
# Exercises : Level 2
def list_of_hexa_colors():
      random_color=random.randint(0,0xFFFFFF)
      print(f"#{random_color:06X}")
list_of_hexa_colors()
def list_of_rgb_colors(n):
      rgb_of_rgb=[]
      j=0
      while j<n:
        i=0
        rgb_list=[]  
        while i<3:
                picked_color=random.randint(0,255)
                rgb_list.append(str(picked_color))
                i+=1
        rgb=','.join(rgb_list)
        print(f"rgb ({rgb})")
        rgb_of_rgb.append(f"rgb({rgb})")
        j+=1
      print(rgb_of_rgb)
list_of_rgb_colors(3)
def list_of_hexa_colors(n):
        i=0
        hexa_list=[]
        while i<n:
                random_color=random.randint(0,0xFFFFFF)
                hexa_list.append(f"#{random_color:06X}")
                i+=1
        print(hexa_list)
def generate_color(color,n):
      if color=='rgb':
            list_of_rgb_colors(n)
      elif color=='hexa':
            list_of_hexa_colors(n)
generate_color('rgb',6)
# Exercises: Level 3
list_test=[1,2,3,4,5]
def shuffle_list(list_sh):
      shuffle_list=[]
      used_index=[]
      while len(shuffle_list)<len(list_sh):
            index=random.randint(0,len(list_sh)-1)
            if index not in used_index:
                  shuffle_list.append(list_sh[index])
                  used_index.append(index)
      print(shuffle_list)
shuffle_list(list_test)
def random_7():
      i=0
      seven_list=[]
      while i < 7:
            num=random.randint(0,9)
            if num not in seven_list:
                  seven_list.append(num)
                  i+=1
      print(seven_list)
random_7()

