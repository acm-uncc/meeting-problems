using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ACM
{
    class Easy
    {
        static void Main(string[] args)
        {
            string plain = "abcdefghijklmnopqrstuvwxyz";
            string cipher = "ZYXWVUTSRQPONMLKJIHGFEDCBA".ToLower();

            Console.Write("Enter phrase: ");
            string input = Console.ReadLine().ToLower();
            string conversion = "";

            for (int i = 0; i < input.Length; i++)
            {
                
                int index = plain.IndexOf(input[i]);
                conversion += cipher[index];
            }

            Console.WriteLine(conversion);

            Console.ReadLine();
        }
    }
}
