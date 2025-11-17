import com.demo.maven.Calculator;
import org.junit.Assert;
import org.junit.Test;


public class CalculatorTest {
    @Test
    public void addTest(){
        //Calculator calc1 = new Calculator();
        int result = Calculator.add(1,2);
        //calc1.add(1,2);
        //Calculator.add(1,2);

        Assert.assertEquals(3,result);

    }


}
