using UnityEngine;

public class PillarHealth : MonoBehaviour
{
    public int maxHealth = 100;
    private int currentHealth;

    void Start()
    {
        currentHealth = maxHealth;
    }

    public void TakeDamage(int damage)
    {
        currentHealth -= damage;
        if (currentHealth <= 0)
        {
            DestroyPillar();
        }
    }

    void DestroyPillar()
    {
        Destroy(gameObject);
    }
}
