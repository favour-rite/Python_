
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class testGeopoliticalZone {
    String state1 = "Benue";
    String state2 = "Adamawa";
    String state3 = "Imo";
    String state4 = "Lagos";
   

    @Test
    public void testFirstGeoPoliticalZone(){
        for(GeoPoliticalZone zone: GeoPoliticalZone.values()){
            for(String state: zone.getStates()){
                if(state1.equalsIgnoreCase(state)){
                    assertEquals(GeoPoliticalZone.NORTH_CENTRAL, zone, "Benue is in North Central");
                }
            }
        }
        GeoPoliticalZone zone = GeoPoliticalZone.NORTH_CENTRAL;
        String[] states = zone.getStates();
        String reply = "Benue";
        zone.statesInGeopolitical(reply);
        assertEquals(GeoPoliticalZone.NORTH_CENTRAL, states[0], "Benue");

    }

    @Test
    public void testSecondGeoPoliticalZone(){
        GeoPoliticalZone zone = GeoPoliticalZone.NORTH_EAST;
        String[] states = zone.getStates();
        String reply = "Adamawa";
        zone.statesInGeopolitical(reply);
        assertEquals(GeoPoliticalZone.NORTH_EAST, states[1], "Adamawa");
    }
    
}
