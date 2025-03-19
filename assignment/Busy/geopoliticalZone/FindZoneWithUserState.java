public class FindZoneWithUserState{

    public void findStateByResponse(){

        for(GeoPoliticalZone zone : GeoPoliticalZone.values()){
            
            if(zone.getStates().contains("Lagos")){
                System.out.println("Lagos is in " + zone);
            }
        }
    }
}