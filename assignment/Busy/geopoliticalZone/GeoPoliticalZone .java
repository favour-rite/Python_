public enum GeoPoliticalZone {

    NORTH_CENTRAL("Benue","FCT","Kogi","Kwara"," Nasarawa ", "Niger","Plateau"),
    NORTH_EAST("Adamawa","Bauchi","Borno","Gombe","Taraba","Yobe"),
    NORTH_WEST("Jigawa","Kaduna","Kano","Katsina","Kebbi","Sokoto","Zamfara"),
    SOUTH_EAST("Abia","Anambra","Ebonyi","Enugu","Imo"),
    SOUTH_SOUTH("Akwa Ibom","Bayelsa","Cross River","Delta","Edo","Rivers"),
    SOUTH_WEST("Ekiti","Lagos","Ogun","Ondo","Osun","Oyo");
    
    private final String[] states;
    GeoPoliticalZone(String... states){
        this.states = states;
    }
    public String[] getStates(){
        return states;
    }
    void statesInGeopolitical(String reply) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'statesInGeopolitical'");
    }
}


