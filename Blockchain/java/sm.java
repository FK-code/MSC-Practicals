package java;
public class sm{
    public static void main(String[] args){
        Message msg = new Message("Old Data");
        System.out.println(msg.getMessage());
        msg.setMessage("New Data");
        System.out.println(msg.getMessage());
    }
}
class Message{
    String message;
    public Message(String newMessage){
        message = newMessage;
    }

    public void setMessage(String newMessage){
        message = newMessage;
    }

    public String getMessage(){
        return message;
    }
}