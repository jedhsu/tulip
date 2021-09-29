
pub struct Equiv {
    left: &Graph,
    right: &Graph,
}

pub trait Equivalence {
    pub type equivalences;

    fn equivalences() -> Iter<Equivalence>;

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

#[cfg(test)]
mod tests {
    use super::Congruent;

    #[test]
    fn congruences(&self) {
    }

    #[test]
    fn adjoin(&self) {
    }

    #[test]
    fn get_duplicates(&self) {
    }
}
