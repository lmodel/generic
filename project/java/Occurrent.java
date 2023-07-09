package None;

import java.util.List;
import lombok.*;






/**
  A processual entity that has temporal parts and happens, unfolds or develops through time. Occurrents have phases. universal:Occurrent is most consistently used as a mixin thus it should be declared as such and cannot inherit from the non-mixin universal:NamedThing
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Occurrent extends TangibleEssenceOrOccurrent {


}