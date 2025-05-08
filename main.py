import streamlit as st
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "Jump@123",
    database="project"
)
res = con.cursor()

def main():
    st.title("My Crud Operation")
    option = st.sidebar.selectbox("Select an option", ["Create", "Read", "Update", "Delete"])

    # For Create Area

    if option == "Create":
        st.subheader("Create an New Record")
        Name = st.text_input("Enter Name")
        Email = st.text_input("Enter Email")
        City = st.text_input("Enter City")

        if st.button("Add Record"): # Button Name
            
            sql = "insert into details(Name,Email,City) values (%s,%s,%s)"
            res.execute(sql,(Name,Email,City))
            con.commit()
            st.success("Record added successfully")

    # For Read Area
    elif option == "Read":
        st.subheader("Read Records")
        
        res.execute("select * from details")
        data = res.fetchall()

        st.table(data) # used to view in table format

    # For Update Area 

    elif option == "Update":
        st.subheader("Update a Record")

        id = st.text_input("Enter ID of the record to update")
        Name = st.text_input("Enter New Name")
        Email = st.text_input("Enter New Email")
        City = st.text_input("Enter New City")

        if st.button("Update Record"): # Button Name

            sql = "update details set Name=%s, Email=%s, City=%s where id=%s"
            res.execute(sql,(Name,Email,City,id))
            con.commit()
            st.success("Record updated successfully")

    # For Delete Area

    elif option == "Delete":
        st.subheader("Delete a Record")

        id = st.text_input("Enter ID of the record to delete")
        if st.button("Delete Record"): # Button Name

            sql = "delete from details where id=%s"
            res.execute(sql,(id,)) # if oru parameter irundha we need to use comma
            con.commit()
            st.success("Deleted Successfully")
        
    else:
        st.error("Error: Invalid option selected")




if __name__ == "__main__":
    main()
