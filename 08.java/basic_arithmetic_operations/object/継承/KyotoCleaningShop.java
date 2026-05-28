package basic_arithmetic_operations.CleaningSevis;


// インターフェースを継承したクラスの定義
public class KyotoCleaningShop implements
ClenningService{
    String ownername;
    String address;
    String phone;
    // シャツを洗う
    public Shirt washShirt(shirt s){
        // 大型洗濯機15分
        return s;
    }

    // タオルを洗う
    public Towl washTowl(Towl t){
        // 大型洗濯機10分
        return t;
    }

    public Coat washCoat(Coat c){
        return c;
    }
}
