
pub struct Congruence {
    left: &Graph,
    right: &Graph,
}

pub trait Congruent {
    pub type congruences;

    fn congruences() -> Iter<Congruence>;

    /// Declares congruences.
    fn adjoin(&self);
    
    fn get_duplicates(graphs: Substitution);


}

impl Congruent for Substitution {
    /// clean this fucking syntax
    fn congruences() -> Iter<Congruence> {
        get_duplicates().iter().map(|x| if let tests.iter().all(|x, y| x.equiv(y)) self.congruences.add(Congruence(x, y));
    }

}
