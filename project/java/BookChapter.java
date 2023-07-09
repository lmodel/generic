package None;

import java.util.List;
import lombok.*;







@Data
@EqualsAndHashCode(callSuper=false)
public class BookChapter extends Publication {

  private String publishedIn;
  private String volume;
  private String chapter;

}