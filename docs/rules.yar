rule prueba
{
    meta:
         Autor = "Dylan Meca"

    strings:
         $a1 = "inner.tlauncher.properties"
    condition:
         $a1

}
