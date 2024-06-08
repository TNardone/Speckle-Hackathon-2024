using UnityEngine;
using UnityEngine.AI;

public class EnemyAI : MonoBehaviour
{
    public float detectionRadius = 10f;
    public float attackDistance = 2f;
    public float attackInterval = 1f;
    public int attackDamage = 10;
    public float randomMoveRadius = 1f; // Radius for random movement
    public float randomMoveInterval = 0.5f; // Time between random movements

    private Transform targetPillar;
    private NavMeshAgent navAgent;
    private float attackTimer;
    private float randomMoveTimer;
    private Vector3 randomMoveTarget;

    void Start()
    {
        navAgent = GetComponent<NavMeshAgent>();
        attackTimer = attackInterval;
        randomMoveTimer = randomMoveInterval;
        FindClosestPillar();
    }

    void Update()
    {
        if (targetPillar == null)
        {
            FindClosestPillar();
            return;
        }

        float distance = Vector3.Distance(transform.position, targetPillar.position);
        
        if (distance <= attackDistance)
        {
            navAgent.isStopped = true;
            AttackPillar();
            PerformRandomMove();
        }
        else
        {
            navAgent.isStopped = false;
            navAgent.SetDestination(targetPillar.position);
        }
    }

    void FindClosestPillar()
    {
        GameObject[] pillars = GameObject.FindGameObjectsWithTag("Pillar");
        float closestDistance = detectionRadius;

        foreach (GameObject pillar in pillars)
        {
            float distance = Vector3.Distance(transform.position, pillar.transform.position);
            if (distance < closestDistance)
            {
                closestDistance = distance;
                targetPillar = pillar.transform;
            }
        }

        if (closestDistance == detectionRadius)
        {
            targetPillar = null; // No pillar found within the detection radius
        }
    }

    void AttackPillar()
    {
        attackTimer -= Time.deltaTime;

        if (attackTimer <= 0f)
        {
            // Perform attack
            PillarHealth pillarHealth = targetPillar.GetComponent<PillarHealth>();
            if (pillarHealth != null)
            {
                pillarHealth.TakeDamage(attackDamage);
            }

            attackTimer = attackInterval;
        }
    }

    void PerformRandomMove()
    {
        randomMoveTimer -= Time.deltaTime;
        if (randomMoveTimer <= 0f)
        {
            // Generate a random position within the random move radius
            Vector2 randomPoint = Random.insideUnitCircle * randomMoveRadius;
            randomMoveTarget = targetPillar.position + new Vector3(randomPoint.x, 0, randomPoint.y);
            randomMoveTimer = randomMoveInterval;
        }

        // Move towards the random move target
        if (Vector3.Distance(transform.position, randomMoveTarget) > 0.1f)
        {
            navAgent.isStopped = false;
            navAgent.SetDestination(randomMoveTarget);
        }
        else
        {
            navAgent.isStopped = true;
        }
    }
}
