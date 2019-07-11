package Contact_Java_project;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Directory {
	
	private Phone p;
	private Sim s;
	private GoogleAccount g;

	public Directory()
	{
		p=new Phone();
		s=new Sim();
		g=new GoogleAccount();
		
		try
		{
			p.take_backup();
			s.take_backup();
			g.take_backup();
		}
		catch(IOException e)
		{
		}
	}
	public boolean working(int ch) throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		if(ch==1)
		{
			System.out.print("\nEnter Search Mode :\n\n1.Search By Name\n2.Search by Number\n3.Search by Email ID\n\nEnter Your Choice : ");
			int sc=Integer.parseInt(br.readLine());
			
			if(sc==1)
			{
				System.out.print("\nEnter Name : ");
				String name=br.readLine();
				
				if(p.search_contact(name,sc) == false)
				{
					if(s.search_contact(name,sc)==false)
					{
						if(g.search_contact(name,sc)==false)
							return false;
					}
				}
			}
			
			else if(sc==2)
			{
				System.out.print("\nEnter Number : ");
				String number=br.readLine();
				
				if(p.search_contact(number,sc) == false)
				{
					if(s.search_contact(number,sc)==false)
					{
						if(g.search_contact(number,sc)==false)
							return false;
					}
				}
			}
			
			else if(sc==3)
			{
				System.out.print("\nEnter Email ID : ");
				String email=br.readLine();
				
				if(p.search_contact(email,sc) == false)
				{
					if(s.search_contact(email,sc)==false)
					{
						if(g.search_contact(email,sc)==false)
							return false;
					}
				}
			}
			return true;
		}
		else if(ch==2)
		{
			System.out.print("\nEnter Search Mode :\n\n1.Search By Name\n2.Search by Number\n3.Search by Email ID\n\nEnter Your Choice : ");
			int dc=Integer.parseInt(br.readLine());
			
			if(dc==1)
			{
				System.out.print("\nEnter Name : ");
				String name=br.readLine();
				
				if(p.delete_contact(name,dc) == false)
				{
					if(s.delete_contact(name,dc)==false)
					{
						if(g.delete_contact(name,dc)==false)
							return false;
					}
				}
			}
			
			else if(dc==2)
			{
				System.out.print("\nEnter Number : ");
				String number=br.readLine();
				
				if(p.delete_contact(number,dc) == false)
				{
					if(s.delete_contact(number,dc)==false)
					{
						if(g.delete_contact(number,dc)==false)
							return false;					}
				}
			}
			
			else if(dc==3)
			{
				System.out.print("\nEnter Email ID : ");
				String email=br.readLine();
				
				if(p.delete_contact(email,dc) == false)
				{
					if(s.delete_contact(email,dc)==false)
					{
						if(g.delete_contact(email,dc)==false)
							return false;
					}
				}
			}
			return true;
		}
		else
		{
			System.out.print("\nEnter Search Mode :\n\n1.Search By Name\n2.Search by Number\n3.Search by Email ID\n\nEnter Your Choice : ");
			int ec=Integer.parseInt(br.readLine());
			
			if(ec==1)
			{
				System.out.print("\nEnter Name : ");
				String name=br.readLine();
				
				if(p.edit_contact(name,ec) == false)
				{
					if(s.edit_contact(name,ec)==false)
					{
						if(g.edit_contact(name,ec)==false)
							return false;
					}
				}
			}
			
			else if(ec==2)
			{
				System.out.print("\nEnter Number : ");
				String number=br.readLine();
				
				if(p.edit_contact(number,ec) == false)
				{
					if(s.edit_contact(number,ec)==false)
					{
						if(g.edit_contact(number,ec)==false)
							return false;
					}
				}
			}
			
			else if(ec==3)
			{
				System.out.print("\nEnter Email ID : ");
				String email=br.readLine();
				
				if(p.edit_contact(email,ec) == false)
				{
					if(s.edit_contact(email,ec)==false)
					{
						if(g.edit_contact(email,ec)==false)
							return false;
					}
				}
			}
			return true;
		}
	}
	public void user_input() throws IOException
	{
		int ch;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		do
		{
			System.out.print("\n1.Add Contact\n2.Search Contact\n3.Display Contacts\n4.Delete Contact\n5.Edit Contact\n6.Exit\n\nEnter Your Choice : ");
			ch=Integer.parseInt(br.readLine());
			
			switch(ch)
			{
				case 1 :
					
					System.out.print("\nEnter Location :\n\n1.Phone\n2.Sim\n3.Google Account\n\nEnter Your Choice : ");
					int l=Integer.parseInt(br.readLine());
					
					if(l==1)
					{
						p.add_contact();
						p.display_contact();
					}
					else if(l==2)
					{
						s.add_contact();
						s.display_contact();
					}
					else
					{
						g.add_contact();
						g.display_contact();
					}
										
					break;
					
				case 2:
					if(working(1)==false)
						System.out.println("\nCONTACT NOT FOUND");
					break;
					
				case 3:
					
					System.out.print("\nEnter Location :\n\n1.Phone\n2.Sim\n3.Google Account\n\nEnter Your Choice : ");
					int ds=Integer.parseInt(br.readLine());
					
					if(ds==1)
						p.display_contact();
					else if(ds==2)
						s.display_contact();
					else if(ds==3)
						g.display_contact();
					
					break;
					
				case 4:
					
					if(working(2)==true)
						System.out.println("\nCONTACT DELETED");
					else
						System.out.println("\nCONTACT NOT FOUND");
					break;
				
				case 5:
					if(working(3)==true)
						System.out.println("\nCONTACT EDITED");
					else
						System.out.println("\nCONTACT NOT FOUND");
					break;
				
				case 6:
					
					p.update_file();
					s.update_file();
					g.update_file();
					System.out.println("\nTHANK YOU");
					break;
					
				default:
					System.out.println("\nWRONG CHOICE");
					break;
			}
			
		}while(ch!=6);
	}
}
