package markdown.other;

import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class SocketServer {
    public static void main(String[] args) throws Exception {
        // 监听指定的端口
        int port = 8080;
        ServerSocket server = new ServerSocket(port);
        Socket socket = server.accept();
        InputStream inputStream = socket.getInputStream();
        byte[] bytes = new byte[1024];
        int len;
        while ((len = inputStream.read(bytes)) != -1) {
            String message = new String(bytes, 0, len, "UTF-8");
            System.out.println(message);
        }
        socket.close();
        server.close();
    }
}
