# Import python packages
import streamlit as st

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
  """Choose fruits you want in your custom smoothie !!
  """
)

cnx = st.connection("snowflake")
session =cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select('FRUIT_NAME')
#st.dataframe(data=my_dataframe, use_container_width=True)

name_on_order = st.text_input("Name on Smoothie:")
st.write('Then name on smoothie will be :'+ name_on_order )
ingredients_list = st.multiselect('Choose upto 5 ingredients:',my_dataframe,max_selections=5)

ingredients_string=''
if ingredients_list:
    for fruits_choosen in ingredients_list:
        ingredients_string+= fruits_choosen + ' '

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order) values ('""" + ingredients_string + """','""" + name_on_order + """')"""


    time_to_insert = st.button("Submit Order")
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success("Your Smoothie is orderd, " + name_on_order + "!", icon='✅')

        
