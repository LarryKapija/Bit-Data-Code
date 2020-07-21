using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace data_CChar
{
    class Program
    {
        static void Main()
        {
            sbyte x = 0, z = 0;
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\User\Documents\Project\Date & Climate.csv");
            int y = lines.Count();
            string[] ToWrite = new string[y];
            string data;
               
            foreach (string line in lines)
            {
                
                if (x > 0 && x < y)
                {
                    data = line.Substring(0, 4);
                    long longbit = ConvertBin(data, 0b101111);

                    data = line.Substring(5, 2);
                    long plusbit = ConvertBin(data, 0b101011);
                    longbit = Xor(longbit, plusbit);

                    data = line.Substring(8, 2);
                    plusbit = ConvertBin(data, 0b100110);
                    longbit = Xor(longbit, plusbit);

                    data = line.Substring(11, 2);
                    plusbit = ConvertBin(data, 0b100001);
                    longbit = Xor(longbit, plusbit);

                    data = line.Substring(14, 2);
                    plusbit = ConvertBin(data, 0b11011);
                    longbit = Xor(longbit, plusbit);

                    data = line.Substring(17, 2);
                    plusbit = ConvertBin(data, 0b10101);
                    longbit = Xor(longbit, plusbit);

                    data = line.Substring(20, 3);
                    plusbit = ConvertBin(data, 0b1011);
                    longbit = Xor(longbit, plusbit);

                    data = line.Substring(24, 2);
                    plusbit = ConvertBin(data, 0b0110);
                    longbit = Xor(longbit, plusbit);

                    data = line.Substring(27, 2);
                    plusbit = ConvertBin(data, 0b0);
                    longbit = Xor(longbit, plusbit);

                    //========================================
                    data = line.Substring(30, 2);
                    int longtemp = ConvertTemp(data, 0b1110);

                    data = line.Substring(33, 2);
                    int shorttemp = ConvertTemp(data, 0b0111);
                    longtemp = longtemp ^ shorttemp;

                    data = line.Substring(36, 2);
                    shorttemp = ConvertTemp(data, 0b0);
                    longtemp = longtemp ^ shorttemp;

                    string[] array = { longbit.ToString(), longtemp.ToString() };
                    string str = string.Join(",", array);
                    ToWrite[z] = str;
                    Console.WriteLine(ToWrite[z]);

                }
                
                System.IO.File.WriteAllLines(@"C:\Users\User\Documents\Project\Bit .csv", ToWrite);

                z++;
                x++;
                //----------------------------------------
            }
            
            Console.ReadKey();  
        }
        public static long ConvertBin(string data, int bit)
        {
            long bin = int.Parse(data);
            bin = bin << bit;
            return bin;
        }
        public static long Xor(long longbit, long bitspace)
        {
            longbit = longbit ^ bitspace;
            return longbit;
        }
        public static int ConvertTemp(string data, int bit)
        {
            int bin = int.Parse(data);
            bin = bin << bit;
            return bin;
        }


    }
}
