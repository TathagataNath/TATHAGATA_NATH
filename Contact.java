package Contact_Java_project;

class Contact 
{
	private String name;
	private String number;
	private String email;
	
	public Contact(String a,String b)
	{
		name=a;
		number=b;
	}
	
	public Contact(String a,String b,String c)
	{
		name=a;
		number=b;
		email=c;
	}
	
	
	public void set_name(String name)
	{
		this.name=name;
	}
	
	public void set_number(String number)
	{
		this.number=number;
	}
	
	public void set_email(String email)
	{
		this.email=email;
	}
	
	public String get_name()
	{
		return name;
	}
	
	public String get_number()
	{
		return number;
	}
	
	public String get_email()
	{
		return email;
	}
	
	public void display()
	{
		System.out.println("\nNAME : "+name+"\nNUMBER : "+number+"\nEMAIL : "+email);
	}
}