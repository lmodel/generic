package None;

import java.util.List;
import lombok.*;






/**
  A written composition in prose, usually nonfiction, on a specific topic, forming an independent part of a book or other publication
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Article extends Publication {

  private String publishedIn;
  private String isoAbbreviation;
  private String volume;
  private String issue;

}