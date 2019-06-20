import java.util.*;
import java.lang.*;
import java.io.*;
public class Prefix
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		String s[]=new String[n];
		for(int i=0;i<n;i++)
		{
			s[i]=sc.next();
		}
		int k=s[0].length();
		for(int i=1;i<n;i++)
		{
			char ch[]=s[i-1].toCharArray();
			char ch1[]=s[i].toCharArray();
			int m=s[i-1].length();
			int o=s[i].length();
			if(m<=o&&m<k)
			{
				k=m;
			}
			if(m>o&&o<k)
			{
				k=o;
			}
			for(int j=0;j<k;j++)
			{
				
				if(ch[j]!=ch1[j])
				{
					k=j;
					j=k;
				}
			}
		}
		char ch[]=s[0].toCharArray();
		for(int i=0;i<k;i++)
		{
			System.out.print(ch[i]);
		}
	}
}
