using System;
class Cadena
{
    static void Main()
    {
        // Comentario de línea de prueba
        string cadena = "Esto Es Una Prueba";
        bool contieneA = cadena.contains("a"); // Variable booleana
        if (contieneA)
        {
            Console.WriteLine("La cadena contiene 'a'");
            return;
        }
        Console.WriteLine("La cadena no contiene 'a'");
    }
}