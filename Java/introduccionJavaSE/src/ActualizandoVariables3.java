public class ActualizandoVariables3 {
    public static void main(String[] args) {
        int salary = 1000;
        //Podemos reutilizar la variable salary para añadirle un bono de 200 dollares
        salary = salary + 200;
        System.out.println(salary);
        //SI queremos descontarle por ejemplo 50 solares:
        salary = salary - 50;
        System.out.println(salary);

        //2 horas extra $3 c/u
        //Comida: $45

        salary = salary + (30*2) - 45;
        System.out.println(salary);

        //ACTUALIZANDO CADENAS DE TEXTO

        String employeeName = "Ruben Pedroche";
        employeeName = employeeName + " Ranz";
        System.out.println(employeeName);

    }
}
