import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LogDemo {
    public static void main(String[] args) {
        Logger logger = LoggerFactory.getLogger(LogDemo.class);


        logger.info("This is info");
        logger.warn("This is warn");
        logger.error("This is error");


        int n = 2;

        if(n > 2){
            System.out.println("n is greater than 2");
        } else {
            System.out.println("n is less than 2");
            logger.info("n is less than or equal to 2");
        }

    }
}
