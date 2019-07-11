package Contact_Java_project;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Phone implements OverrideMethords 
{
	private FileReader fr;
	private BufferedReader br1,br2=new BufferedReader(new InputStreamReader(System.in));
	private FileWriter fw;
	private BufferedWriter bw;
	ArrayList<Contact> c=new ArrayList<Contact>();
	
	public void take_backup() throws IOException
	{
		fr=new FileReader("C:\\Users\\USER\\Desktop\\Contact_project\\Phone.txt");
		br1=new BufferedReader(fr);

		String t;
		while((t=br1.readLine())!=null)
		{
			String []s=t.split(",");
			String name=s[0];
			String num=s[1];
			String email=s[2];
			
			Contact ob;
			if(email.equals(""))
				ob=new Contact(name, num);
			else
				ob=new Contact(name, num, email);
			
			c.add(ob);
		}
		br1.close();
	}

	public void add_contact() throws IOException
	{
		Contact ob;
		
		System.out.print("\nEnter Name : ");
		String name=br2.readLine();
		System.out.print("\nEnter Number : ");
		String number=br2.readLine();
		System.out.print("\nDo You Want To Add Email :\n1.Yes\n2.No\n\nEnter Your Choice : ");
		int ch=Integer.parseInt(br2.readLine());
		if(ch==1)
		{
			System.out.print("\nEnter Email : ");
			String email=br2.readLine();
			
			ob=new Contact(name, number, email);
		}
		else
			ob=new Contact(name, number);
		
		c.add(ob);
		System.out.println("\nCONTACT ADDED");
	}

	public Contact get_contact(String str,int ch)
	{
		for(int i=0;i<c.size();i++)
		{
			if(ch==1)
			{
				if(c.get(i).get_name().equalsIgnoreCase(str))
					return c.get(i);
			}
			else if(ch==2)
			{
				if(c.get(i).get_number().equalsIgnoreCase(str))
					return c.get(i);

			}
			else
			{
				if(c.get(i).get_email().equalsIgnoreCase(str))
					return c.get(i);
			}
		}
		return null;
	}
	
	public boolean search_contact(String str,int ch)
	{
		Contact ob=get_contact(str, ch);
		if(ob!=null)
		{
			ob.display();
			return true;
		}
		else
			return false;
	}
	
	public void display_contact() 
	{
		for(int i=0;i<c.size();i++)
		{
			Contact ob=c.get(i);
			ob.display();
		}
	}

	public boolean delete_contact(String str,int ch) 
	{
		Contact ob=get_contact(str, ch);
		if(ob!=null)
		{
			ob.display();
			c.remove(ob);
			return true;
		}
		else
			return false;
	}
	
	public boolean edit_contact(String str,int ch) throws IOException
	{
		Contact ob=get_contact(str, ch);
		if(ob==null)
			return false;
		else
		{
			System.out.print("\n1.Edit Name\n2.Edit Number\n3.Edit Email ID\n\nEnter Your Choice : ");
			int m=Integer.parseInt(br2.readLine());
			
			if(m==1)
			{
				System.out.print("\nEnter New Name : ");
				String name=br2.readLine();
				ob.set_name(name);
			}
			else if(m==2)
			{
				System.out.print("\nEnter New Number : ");
				String number=br2.readLine();
				ob.set_number(number);
			}
			else if(m==3)
			{
				System.out.print("\nEnter New Email ID : ");
				String email=br2.readLine();
				ob.set_email(email);
			}
			return true;
		}
	}

	public void update_file() throws IOException
	{
		fw=new FileWriter("C:\\Users\\USER\\Desktop\\Contact_project\\Phone.txt");
		bw=new BufferedWriter(fw);
		
		for(int i=0;i<c.size();i++)
		{
			Contact ob=c.get(i);
			String name=ob.get_name();
			String number=ob.get_number();
			String email=ob.get_email();
			
			bw.write(name+","+number+","+email);
			bw.write("\n");
			//bw.flush();
		}
		bw.close();
	}

}
