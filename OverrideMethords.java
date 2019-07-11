package Contact_Java_project;

import java.io.IOException;

public interface OverrideMethords 
{
	public void take_backup() throws IOException;
	public void add_contact() throws IOException;
	public boolean search_contact(String str,int ch);
	public void display_contact();
	public boolean delete_contact(String str,int ch);
	public boolean edit_contact(String str,int ch) throws IOException;
	public Contact get_contact(String str,int ch);
	public void update_file() throws IOException;
}
