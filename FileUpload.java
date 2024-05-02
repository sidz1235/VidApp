import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class FileUpload {

    public static void main(String[] args) {
        String endpointUrl = "http://localhost:5000/upload";
        String videoFilePath = "C:\\Users\\dsidd\\Desktop\\vid\\app\\WIN_20240412_11_47_16_Pro.mp4";

        try {
            URL url = new URL(endpointUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);

            String boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW";

            connection.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + boundary);

            OutputStream outputStream = connection.getOutputStream();
            PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);

            // File
            writer.append("--" + boundary).append("\r\n");
            writer.append("Content-Disposition: form-data; name=\"file\"; filename=\"" + videoFilePath + "\"").append("\r\n");
            writer.append("Content-Type: video/mp4").append("\r\n");
            writer.append("\r\n");
            writer.flush();

            FileInputStream inputStream = new FileInputStream(videoFilePath);
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
            }
            outputStream.flush();
            inputStream.close();

            writer.append("\r\n").flush();
            writer.append("--" + boundary + "--").append("\r\n");
            writer.close();

            int responseCode = connection.getResponseCode();
            System.out.println("Response Code: " + responseCode);

            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            System.out.println("Response: " + response.toString());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
